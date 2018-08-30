#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:25:24 2018

@author: DennisLin
"""

from subprocess import Popen, PIPE


def call_function(input_sentence):
    process.stdin.write((input_sentence+'\n').encode())
    process.stdin.flush()
    for line in iter(process.stdout.readline, b''):
        if line == 'End\n'.encode():
            break
        qa_list = line.decode().split('\n')[0].split('?')
        print(qa_list[0])
        if not qa_list[1]:
            print(unicode('yes', "utf-8"))
        else:
            print(qa_list[1])

                        
if __name__ == '__main__':
    command = ['bash', 'run.sh']
    process = Popen(command, bufsize = 1, stdin = PIPE, stdout = PIPE)
    while True:
        input_sentence = raw_input("Input sentence:")
        if input_sentence == 'q':
            break
        call_function(input_sentence)
    