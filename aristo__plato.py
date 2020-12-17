##################################################
# this code implements a basic bot using
# twitter API - this is the main file that
# runs the bot: it gets data from a pre
# populated csv file and updates the status
# with random tweets
#
# filename: aristo__plato
# author: mrbacco 2020
##################################################

import tweepy
import csv
import logging
# from config import tw_api
import random
from datetime import datetime
import time
import re



###################### logger setup START ######################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###################### logger setup END ######################

###################### tw_api function START ######################
# this is a function that returns the api so that we can
# do everything using it, reading and writing for example

def tw_api():
    # performing authentication and verifying it
    auth = tweepy.OAuthHandler("xxx", "xxx")
    auth.set_access_token("xxx-,xxx",
                          "xxx")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error while creating API", exc_info=True)
        raise e
    logger.info("tw_api successfully created")
    return api


###################### tw_api function END ######################

###################### auth START ######################
'''
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
'''

# test tweet
# api.update_status("The greatest wealth is to live content with little")

###################### auth END ######################

###################### reading timeline START ######################

'''
t_line = api.home_timeline()
for tweet in t_line:
    logger.info("timelines tweets are: ", f"{tweet.user.name} said {tweet.text}")
'''


###################### reading timeline END ######################


"""
###################### cleaning tweets START ######################

def clean_tweet(tweets): # function to clean tweet text by removing links, special characters using regex
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) (\w+:\/\/\S+)", " ", tweets).split())


###################### cleaning tweets START ######################

###################### load source START ######################


with open("source.csv", encoding='iso-8859-1') as data:
    tweets = csv.reader(data)
    clean_tweet(tweets)
    print(tweets)

###################### load source END ######################
"""

###################### Tweet update START ######################

with open('source.csv', "r", errors="ignore", newline='') as f1:
    spamreader = csv.reader(f1, delimiter=',')
    source=[i for row in spamreader for i in row]

with open('adjectives.txt', "r") as f2:
    spamreader = csv.reader(f2, delimiter=',')
    adj=[i for row in spamreader for i in row]

print(len(source))
print(len(adj))

marks = ["!", ".", ".", "?", ".", "!!!", ".", ".", "."]

n = 1
while n >= 0:

    num1 = random.randrange(0,67248)    # source
    num2 = random.randrange(0,9)        # marks
    num3 = random.randrange(0,5301)     # adj
    num4 = random.randrange(0,5301)     # adj2

    x = random.randrange(0,12)

    now = str(datetime.now().replace(microsecond=0))
    
    sentence1 = ("%s %s "%(random.choice(source), random.choice(adj)))
    sentence2 = (adj[num3] + ": " + source[num1] + " " + marks[num2])
    sentence3 = (now + ": thought of the moment ... " + adj[num4])

    #print(sentence1 + "\n")
    #print(sentence2 + "\n")
    #print(sentence3 + "\n")

    if x % 3 ==0:
        print("\n", "1 ... status update with: ", "\n",sentence1)
        api.update_status(sentence1)
        print("x = " + str(x))
        time.sleep(244)
    
    if x % 5 ==0:
        print("\n", "2 ... status update with: ", "\n",sentence2)
        api.update_status(sentence2)
        print("x = " + str(x))
        time.sleep(60*43)

    else:
        print("\n", "3 ... status update with: ", "\n",sentence3)
        api.update_status(sentence3)
        print("x = " + str(x))
        time.sleep(4442)



###################### Tweet update END ######################
