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

###################### def main START ######################

def main():
    with open("source.csv",  mode='r', errors="ignore") as data:
        reader = csv.reader(data)
        for index, row in enumerate(reader):

            if index != 0:
                now = str(datetime.now())
                chosen_row = row
                # api.update_status(chosen_row + [" - ", now])
                print("Hey, updated status with: ", chosen_row + [" - ", now])
                time.sleep( 0 )  # wait before tweeting again
            '''
            else:
                r = random.randint(0, index)
                print(row)
                if r >= 0:
                    now = str(datetime.now())
                    api.update_status(row + [" - ", now])
                    print("else updated status with: ", row, r, now)
                    time.sleep(60 * 60 )  # wait before tweeting again
            '''

###################### def main END ######################


###################### running the application ######################
if __name__ == "__main__":
    main()


