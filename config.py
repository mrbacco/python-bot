##################################################
# this code implements a basic bot using
# twitter API - this file is for configuration
# of the API connection
#
# filename: config
# author: mrbacco 2020
##################################################

import tweepy
import logging

###################### logger setup START ######################

logger = logging.getLogger()

###################### logger setup END ######################



###################### tw_api function START ######################
# this is a function that returns the api so that we can
# do everything using it, reading and writing for example

def tw_api():
    # performing authentication and verifying it
    auth = tweepy.OAuthHandler("4iABPJcUW82h7W6c767Vg88ed", "VwFpjzoRDnffpunYx5dPN5FiE8IoHhv1h26lEzP0Ug4IslnAL1")
    auth.set_access_token("1271435160832139264-6HqwVaMSPsuvycwwdFOz8LkSqX0XU3",
                          "Jb8Zf586OZAkJuYwh6MeqYESJ7rXqjXZtOpJBqYfDcSyv")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error while creating API", exc_info=True)
        raise e
    logger.info("tw_api successfully created")
    return api


###################### tw_api function END ######################

