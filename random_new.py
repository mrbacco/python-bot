##################################################
# this code implements a basic bot using
# twitter API - this file is for random
# generation of strings
#
# filename: random_new
# author: mrbacco 2020
##################################################


import random
import json
import pandas as pd

data = pd.read_csv("source.csv", encoding= 'unicode_escape')
# d = data["text"]["from"]
print(data.head())
print(data)


