#!/usr/bin/python
# -*- coding:utf-8 -*-
# **************************
# * Author      :  baiyyang
# * Email       :  baiyyang@163.com
# * Description :  实现bleu，支持计算中文和英文
# * create time :  2018/5/11下午3:47
# * file name   :  bleu.py


import os
import argparse
import math


def read_data(candidate_filename, reference_file):
    """
    读取候选文件和参考文件
    :param candidate_filename: 候选文件
    :param reference_file: 参考文件，可以为文件夹，或者是单个的文件
    :return:
    """
    candidates = []
    references = []
    with open(candidate_filename, "r", encoding="utf-8") as fr:
        for line in fr:
            candidates.append(line.strip())
    if ".txt" in reference_file:
        with open(reference_file, "r", encoding="utf-8") as fr:
            reference = []
            for line in fr:
                reference.append(line.strip())
            references.append(reference)
    else:
        for root, _, files in os.walk(reference_file):
            for file in files:
                reference = []
                with open(os.path.join(root, file), "r", encoding="utf-8") as fr:
                    for line in fr:
                        reference.append(line.strip())
                references.append(reference)
    return candidates, references


def calculate_ngram(candidates, references, n, language):
    count_clip = 0
    count = 0
    for index, candidate in enumerate(candidates):
        references_list = lines2dic(references, index, n, language)
        if language == "en":
            words = candidate.split()
        else:
            words = candidate
        limit = len(words) - n + 1
        candidate_dic = {}
        for i in range(limit):
            key = " ".join(words[i: i+n]).lower() if language == "en" else words[i: i+n]
            if key in candidate_dic.keys():
                candidate_dic[key] += 1
            else:
                candidate_dic[key] = 1
        count_clip += clip(candidate_dic, references_list)
        count += limit
    if count_clip == 0:
        pr = 0
    else:
        pr = float(count_clip) / count
    return pr


def brevity_penalty(candidates, references, language):
    c = 0
    r = 0
    for index, candidate in enumerate(candidates):
        c_length = len(candidate.split()) if language == "en" else len(candidate)
        reference_index = [reference[index] for reference in references]
        r_lengths = [len(r.split()) if language == "en" else len(r) for r in reference_index]
        c += c_length
        r += match_reference(c_length, r_lengths)
    if c > r:
        bp = 1
    else:
        bp = math.exp(1 - float(r) / c)
    return bp


def match_reference(candidate_len, reference_lens):
    """
    计算当c<=r时，最佳匹配的r的长度
    :param candidate_len:
    :param reference_lens:
    :return:
    """
    best_len = abs(reference_lens[0] - candidate_len)
    best_ref = reference_lens[0]
    for length in reference_lens:
        if abs(length - candidate_len) < best_len:
            best_len = abs(length - candidate_len)
            best_ref = length
    return best_ref


def clip(candidate, references):
    count = 0
    for cand in candidate.keys():
        cand_value = candidate[cand]
        max_count = 0
        for reference in references:
            if cand in reference.keys():
                max_count = max(reference[cand], max_count)
        count += min(max_count, cand_value)
    return count


def lines2dic(references, index, n, language):
    reference_list = []
    for reference in references:
        reference_dic = {}
        line = reference[index]
        if language == "en":
            words = line.split()
        else:
            words = line
        limit = len(words) - n + 1
        for i in range(limit):
            key = " ".join(words[i: i+n]).lower() if language == "en" else words[i: i+n]
            if key in reference_dic.keys():
                reference_dic[key] += 1
            else:
                reference_dic[key] = 1
        reference_list.append(reference_dic)
    return reference_list


def geometric_mean(precisions):
    return math.exp(sum([math.log(p) if p != 0 else -math.inf for p in precisions]) / len(precisions))


def bleu(candidate, references, language):
    precisions = []
    for i in range(1, 5):
        pr = calculate_ngram(candidate, references, i, language)
        precisions.append(pr)
    bp = brevity_penalty(candidate, references, language)
    return geometric_mean(precisions) * bp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BLEU calculate")
    parser.add_argument("candidate", help="candidate file", type=str)
    parser.add_argument("reference", help="reference file or dir", type=str)
    parser.add_argument("language", help="the language of evaluation, include en/ch", type=str)
    args = parser.parse_args()
    can_file = args.candidate
    ref_file = args.reference
    lang = args.language
    candidate, references = read_data(can_file, ref_file)
    bleu = bleu(candidate, references, lang)
    print("BLEU: {}".format(bleu))

