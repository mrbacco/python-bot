# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:54:52 2020

@author: mrbacco
"""

###################### imports START ######################

import csv
import random
import time
from datetime import datetime
import tweepy
import logging



###################### imports END ######################

###################### logger setup START ######################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###################### logger setup END ######################

###################### tw_api func START ######################

auth = tweepy.OAuthHandler("xxx", "xxx")
auth.set_access_token("xxx-xxx",
                          "xxx")

# API object to use for everything
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    logger.info("logged in, thanks")
except:
    logger.info("errors during authentication, try again")

###################### tw_api func END ######################


###################### Tweet update START ######################

with open('source.csv', "r", errors="ignore", newline='') as f1:
    spamreader = csv.reader(f1, delimiter=',')
    source=[i for row in spamreader for i in row]

with open('adjectives.txt', "r") as f2:
    spamreader = csv.reader(f2, delimiter=',')
    adj=[i for row in spamreader for i in row]

# print(source)
now = str(datetime.now().replace(microsecond=0))

n = 1
while n > 0:
    sentence = ("%s %s "%(random.choice(source), random.choice(adj)))
    print("Hey ... status update with: ", sentence )
    # api.update_status(sentence + now)
    time.sleep(1)

###################### Tweet update END ######################
