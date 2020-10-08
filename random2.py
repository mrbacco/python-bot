# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:37:38 2020

@author: mrbacco
"""

import csv
import random
import time

with open('adverbs.txt', "r") as f1:
    spamreader = csv.reader(f1, delimiter=',')
    adv=[i for row in spamreader for i in row]

with open('adjectives.txt', "r") as f2:
    spamreader = csv.reader(f2, delimiter=',')
    adj=[i for row in spamreader for i in row]
    
with open('nouns.txt', "r") as f3:
    spamreader = csv.reader(f3, delimiter=',')
    nouns=[i for row in spamreader for i in row]
    
with open('verbs.txt', "r") as f4:
    spamreader = csv.reader(f4, delimiter=',')
    verbs=[i for row in spamreader for i in row]
    

print(adv, "\n")
# print(adj, "\n")
# print(nouns, "\n")
# print(verbs, "\n")


n = 1
while n > 0:
    sentence = ("%s %s %s %s"%(random.choice(nouns), random.choice(verbs), 
                               random.choice(adv), random.choice(adj)))
    print(sentence, "\n")
    time.sleep(2)

