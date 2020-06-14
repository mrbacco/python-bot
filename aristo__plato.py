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
from config import tw_api
import time


###################### logger setup START ######################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###################### logger setup END ######################


###################### auth START ######################

auth = tweepy.OAuthHandler()
auth.set_access_token()

# API object to use for everything
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    logger.info("logged in, thanks")
except:
    logger.info("errors during authentication, try again")

# test tweet
# api.update_status("The greatest wealth is to live content with little")

###################### auth END ######################

###################### reading timeline START ######################

t_line = api.home_timeline()
for tweet in t_line:
    logger.info("timelines tweets are: ", f"{tweet.user.name} said {tweet.text}")

###################### reading timeline END ######################


api = tw_api()
logger.info("the api object is: ", str(api))

###################### load source START ######################


with open("source.csv", encoding='iso-8859-1') as data:
    reader = csv.reader(data)

###################### load source END ######################


###################### def main START ######################


def main():
    with open("source.csv", encoding='iso-8859-1') as data:
        reader = csv.reader(data)
        for row in reader:
            print(str(row))
            api.update_status(str(row))
            logger.info("Waiting ...")
            time.sleep(86400*2)  # wait before tweeting again


###################### def main END ######################


###################### running the application ######################
if __name__ == "__main__":
    main()



