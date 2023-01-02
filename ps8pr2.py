#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:38:49 2021

@author: chrisrelyea
"""

import random

def create_dictionary(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    words = text.split()
    
    
    d = {}
    
    current_word = '$'
    
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
            
        if next_word[-1] in '?.!':
            current_word = '$'
        else: 
            current_word = next_word
            
    return d
        

def generate_text(word_dict, num_words):
    current_word = '$'
    for x in range(num_words):
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        
        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    print()
        
        
        
            
        
        
        














    
    
    
    