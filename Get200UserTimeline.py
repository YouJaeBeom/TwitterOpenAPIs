from random import seed
from random import randint
import time
import twitter
import datetime
import json
import logging
import os
from logging.handlers import TimedRotatingFileHandler


class TwitterAPIs:

    """
    Response formats	JSON
    Requires authentication?	Yes
    Rate limited?	Yes
    Requests / 15-min window (user auth)	900
    Requests / 15-min window (app auth)	1500
    Requests / 24-hour window	100,000

    """

    def __init__(self):
        ## twitter api key setting
        self.twitter_consumer_key = "25nwDEFygPN4JrONW52ZRpbkj"
        self.twitter_consumer_secret = "6rcUXU84Mk4Bi4Gp2HTyXR8uJOLDapkKvLvyiNCxNRP7075drq"
        self.twitter_access_token = "1067071463948148736-C3uNvuBgvZ8p83QE8hDv4kONZM593k"
        self.twitter_access_secret = "jBaKhsuXhj1C3SDHFWozubyXoEDQPqw8oWFqaSD5Qi31M"

        self.twitter_api = twitter.Api(consumer_key=self.twitter_consumer_key, consumer_secret=self.twitter_consumer_secret,
                                  access_token_key=self.twitter_access_token, access_token_secret=self.twitter_access_secret)

        ## logger setting
        self.logger=logging.getLogger("log")
        self.logger.setLevel(logging.INFO)
        self.formatter=self.logging.Formatter('%(asctime)s > %(message)s')
        self.fileHandler=self.logging.FileHandler("./final_log.txt")
        self.streamhandler=self.logging.StreamHandler()
        self.fileHandler.setFormatter(self.formatter)
        self.streamhandler.setFormatter(self.formatter)
        self.logger.addHandler(self.fileHandler)
        self.logger.addHandler(self.streamhandler)


    def twitterapis_crawling(self):
        ## starting point time setting
        start_time = datetime.datetime.now()

        ## total accounts list tweet count setting
        total_count=0

        ## accounts list setting
        with open('list.txt', 'r') as f:
            ## accounts list
            accounts = f.read().split(',')

            for account in accounts:
                account="@"+account
                ## tweet save file setting
                file_path = "./tweet_0521/" + account + ".json"
                file_path_id = "./tweet_id_0521/" + account + ".txt"

                start_time = datetime.datetime.now()
                statuses = self.twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=False, exclude_replies=True)
                time.sleep(1)

                ## account tweet count setting
                count = 0
                with open(file_path, 'w') as outfile:
                    with open(file_path_id, 'w') as w:
                        for status in statuses:
                            count = count + 1
                            print(count, "=>", status.id, "=>", status.text, "=>", status.created_at)
                            w.write(str(status.id)+",")
                            outfile.write(str(status)+"\n")
                        total_count=total_count+count
                        end_time = datetime.datetime.now()
                        self.logger.info(f'ID => {account}  count => {count}  time => {(end_time - start_time).seconds}')
                        w.close()
        end_time = datetime.datetime.now()
        self.logger.info(f'FINSH!!!!!! time => {(end_time - start_time).seconds} total_count => {total_count}')

if __name__ == '__main__':
    twitterapis = TwitterAPIs()
    twitterapis.twitterapis_crawling()
