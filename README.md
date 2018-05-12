# BLEU
Calculate the Evaluation of Machine Translate--BLEU，the language includes Chinese and English

BLEU -- BiLingual Evaluation Understudy, is a method to evaluate result of Machine Translate.

## Calculate
1. calculate the _count_clip(n-gram)_
![](https://github.com/baiyyang/BLEU/blob/master/image/count.png)
Where _count(n-gram)_ is the number of occurrences of an n-gram in the candidate translation, and _MaxRefCount(n-gram)_ is the maximum number of occurrences of the n-gram in the reference translation. The final statistical result _count_clip(n-gram)_ is the smaller of the two.
2. calculate the _pn_

<img src="https://github.com/baiyyang/BLEU/blob/master/image/pn.png" width="70%" height="70%" />

3. calculate the _bp_

<img src="https://github.com/baiyyang/BLEU/blob/master/image/bp.png" width="30%" height="30%" />

4. calculate _BLEU_

<img src="https://github.com/baiyyang/BLEU/blob/master/image/bleu.png" width="30%" height="30%" />

## Usage
calculate English BLEU:
>python bleu.py data/candidate_en.txt data/reference_en en

calculate Chinese BLEU:
>python bleu.py data/candidate_ch.txt data/reference_ch ch

## Reference
[BLEU: a Method for Automatic Evaluation of Machine Translation](http://www.aclweb.org/anthology/P02-1040.pdf)

[git:vikasnar/Bleu](https://github.com/vikasnar/Bleu)

