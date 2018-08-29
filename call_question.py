#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:08:40 2018

@author: DennisLin
"""
import os
from subprocess import Popen, PIPE
import json
import joblib as ib
from tqdm import tqdm


def callquestion(label_dict):
    command = ['bash', 'run.sh']
    process = Popen(command, bufsize=1, stdin=PIPE, stdout=PIPE)
    train_question = {}
    train_answer = {}
    for video_id in tqdm(sorted(label_dict)):
#    video_id = 'video102'
        print("Now Processing " + video_id)
        train_question[video_id] = []
        train_answer[video_id] = []
        except_ls = []
        for idx, label_sentence in enumerate(train_label[video_id]):
            process.stdin.write((label_sentence+'\n').encode())
#            print(label_sentence)
            process.stdin.flush()
            out_q = []
            out_a = []
            for line in iter(process.stdout.readline, b''):
                if line == 'End\n'.encode():
                    break    
                qa_list = line.decode().split('\n')[0].split('?')
                out_q.append(qa_list[0])
                if qa_list[1] == '':
                    qa_list[1] = unicode('yes', "utf-8")
                out_a.append(qa_list[1])
            #if no question generated
            if not out_q:
                except_ls.append(idx)
            train_question[video_id].append(out_q)
            train_answer[video_id].append(out_a)
        
        #reprocess the exception
        for except_idx in except_ls:
            input_sentence = train_label[video_id][except_idx]
            
            
            input_sentence_ls = input_sentence.split(' ')
            #case 1: there is/ there are...
            if input_sentence_ls[0] == 'there':
                if input_sentence_ls[1] == 'is':
                    input_sentence_ls[0].replace('there', 'is')
                    input_sentence_ls[1].replace('is', 'there')
                    train_question[video_id][except_idx] = [' '.join(input_sentence_ls)]
                    train_answer[video_id][except_idx] = ['yes']
                elif input_sentence_ls[1] == 'are':
                    input_sentence_ls[0].replace('there', 'are')
                    input_sentence_ls[1].replace('are', 'there')
                    train_question[video_id][except_idx] = [' '.join(input_sentence_ls)]
                    train_answer[video_id][except_idx] = ['yes']
            #case 2: "ing" exsits in verb
            else:
                resend = False
                for idx, sentence in enumerate(input_sentence_ls):
                    if 'ing' in sentence:
                        input_sentence_ls[idx] = sentence[:-3]
                        resend = True
                if resend:
                    process.stdin.write((' '.join(input_sentence_ls)+'\n').encode())
                    process.stdin.flush()
                    out_q = []
                    out_a = []
                    for line in iter(process.stdout.readline, b''):
                        if line == 'End\n'.encode():
                            break    
                        qa_list = line.decode().split('\n')[0].split('?')
                        out_q.append(qa_list[0])
                        if qa_list[1] == '':
                            qa_list[1] = unicode('yes', "utf-8")
                        out_a.append(qa_list[1])
                    if out_q:
                        train_question[video_id][except_idx] = out_q
                        train_answer[video_id][except_idx] = out_a
    process.stdout.close()
    return train_question, train_answer


def load_json(path):
    with open(path) as data_file:    
        path_file = json.load(data_file)
    return path_file


def clean_string(string):
    return string.replace('.', '').replace(',', '').replace('"', '').replace('\n', '').replace('?', '').replace('!', '').replace('\\', '').replace('/', '')


def load_caption(label_path):
    train_label_dict={}    
    train_label = load_json(label_path)
    id_list = []
    for sample in train_label:
        id_list.append(sample['id'])
        cleaned_captions = [clean_string(sentence) for sentence in sample["caption"]]

        train_label_dict[sample["id"]] = cleaned_captions
    return train_label_dict

        
train_label_path = './MSRVTT/training_label.json'
test_label_path = './MSRVTT/testing_label.json'
if __name__ == "__main__":
    train_label = load_caption(train_label_path)
    train_question, train_answer = callquestion(train_label)
    ib.dump(train_question, './train_question.pkl')
    ib.dump(train_answer, './train_answer.pkl')
    test_label = load_caption(test_label_path)
    test_question, test_answer = callquestion(test_label)
    ib.dump(test_question, './test_question.pkl')
    ib.dump(test_answer, './test_answer.pkl')    
    