# Question Generation in NLP
It's a modified code ***[from Michael Heilman](http://www.cs.cmu.edu/~ark/mheilman/questions/)***. The system use NLP to generate question-answer pairs from given sentences. The main function in ```call_question.py``` usualize the Question Generaton system to generate QA-pair for [***MSR-VTT***](http://ms-multimedia-challenge.com/dataset) and save them as ```.json```. 


## Requirement
- Java, follow the [official installation](https://www.oracle.com/technetwork/java/javase/downloads/index.html)
- python 2.7
- MSR-VTT label

## Usage 

You can simply run the question generation part by:
```
bash run.sh
```
If you want to apply it on MSR-VTT dataset, please run the following:
```
python call_question.py
```


## Note
We not only usualize QG system to generate QA pairs, but also deal with exception. Please see the line 46 - 86 for more detail.


## Reference
- [ Automatic Factual Question Generation from Text](http://www.cs.cmu.edu/~ark/mheilman/questions/papers/heilman-question-generation-dissertation.pdf)
- [Question Generation via Overgenerating Transformations and Ranking](http://www.cs.cmu.edu/~ark/mheilman/questions/)
