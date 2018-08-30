# Question Generation in NLP
It's a modified code from [***Michael Heilman***](http://www.cs.cmu.edu/~ark/mheilman/questions/). The system use NLP to generate question-answer pairs from given sentences. The main function in ```call_question.py``` usualize the Question Generaton system to generate QA-pair for [***MSR-VTT***](http://ms-multimedia-challenge.com/dataset) and save them as ```.json```. 


## Requirement
- Java 1.8, follow the [official installation](https://www.oracle.com/technetwork/java/javase/downloads/index.html)
- python 2.7
- MSR-VTT label

## Usage 
1. You can simply run the question generation part by:
```
bash run.sh
```
or you might want to usualize the question generatior as an API and apply on personal work. You could use the ```call_function()``` in ```call_function.py``` as shown in the following:
```python
command = ['bash', 'run.sh']
process = Popen(command, bufsize = 1, stdin = PIPE, stdout = PIPE)
while True:
    input_sentence = raw_input("Input sentence:")
    if input_sentence == 'q':
        break
    call_function(input_sentence)
```
2. If you want to apply it on MSR-VTT dataset, please run the following:
```
python call_question.py
```
To load ```train_question.pkl``` and ```train_answer.pkl``` , please do the following:
```python
import joblib as ib #(version: 0.10.3)
train_question = ib.load('./train_question.pkl')
```
train_question and train_answer is a dictionary use str 'video{id}' as key and List[List[str]] as value.

## Result
For question generation:
```
Input: The man introduces his two dogs.
Questions: 
 [u'Who introduces his two dogs',
  u'How many his dogs does man introduce',
  u'What does man introduce',
  u'Does man introduce his two dogs']
Answers:
[u'man', u'his two dogs', u'his two dogs', u'yes']
```

## Note
We not only usualize QG system to generate QA pairs, but also deal with exception. Please see the line 46 - 86 for more detail.


## Reference
- [ Automatic Factual Question Generation from Text](http://www.cs.cmu.edu/~ark/mheilman/questions/papers/heilman-question-generation-dissertation.pdf)
- [Question Generation via Overgenerating Transformations and Ranking](http://www.cs.cmu.edu/~ark/mheilman/questions/)
