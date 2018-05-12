# BLEU
Calculate the Evaluation of Machine Translate--BLEU，the language includes Chinese and English

BLEU -- BiLingual Evaluation Understudy, is a method to evaluate result of Machine Translate.

## Calculate
1. calculate the _count_clip(n-gram)_
![](https://github.com/baiyyang/BLEU/blob/master/image/count_clip.png)
Where _count(n-gram)_ is the number of occurrences of an n-gram in the candidate translation, and _MaxRefCount(n-gram)_ is the maximum number of occurrences of the n-gram in the reference translation. The final statistical result _count_clip(n-gram)_ is the smaller of the two.
2. calculate the _pn_

![](https://github.com/baiyyang/BLEU/blob/master/image/pn.png)
3. calculate the _bp_

![](https://github.com/baiyyang/BLEU/blob/master/image/bp.png)
4. calculate _BLEU_

![](https://github.com/baiyyang/BLEU/blob/master/image/bleu.png)
## Usage

## Reference

