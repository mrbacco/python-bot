# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:37:38 2020

@author: mrbacco
"""

'''
import random
from random_word import RandomWords
from RandomWordGenerator import RandomWord

r = RandomWords()

r.get_random_word()


# Creating a random word object
rw = RandomWord(constant_word_size=True,
                include_digits=False,
                special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                include_special_chars=False)



nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
num = random(0,5)
# phrase = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
'''

import lorem
import time
import random


s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
p = lorem.paragraph()
t = lorem.text()


n = 1
while n > 0:
    sentence = ("%s "%(random.choice(s)))

    print(str(s))
    time.sleep(2)

