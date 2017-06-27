#!/usr/bin/python

import json
import csv
import sys
from pymongo import MongoClient


def main(argv):

    collect_name = str(argv[0]) + "_datamine"
    client = MongoClient()
    db = client.test_database
    data = getattr(db, collect_name)

    if(len(argv) > 2):
        if(str(argv[2]).lower() == "true"):
            collect2_name = str(argv[1]) + "_datamine"
            data = getattr(db, collect2_name)

    tweets = []
    for tweet in data.find(no_cursor_timeout=True):
        tweets.append(tweet)

    output_tuples = []

    for tweet in tweets:
        my_tuple = []

        # Encodes each hashtag and mention
        hashtags = []
        mentions = []
        for d in tweet['entities']['user_mentions']:
            mentions.append(d['screen_name'].encode('ascii',errors='ignore'))
        for d in tweet['entities']['hashtags']:
            hashtags.append(d['text'].encode('ascii',errors='ignore'))

        my_tuple = (tweet['text'].encode('ascii',errors='ignore'), tweet['user']['screen_name'].encode('ascii',errors='ignore'), tweet['created_at'], hashtags, tweet['entities']['urls'], mentions, tweet['id_str'])
        try:
            my_tuple = my_tuple + (tweet['in_reply_to_status_id_str'],)
        except:
            my_tuple = my_tuple + (' ',)
        try:
            my_tuple = my_tuple + (tweet['in_reply_to_screen_name'],)
        except:
            my_tuple = my_tuple + (' ',)
        try:
            my_tuple = my_tuple + (tweet['place']['country'].encode('ascii',errors='ignore'),)
        except:
            my_tuple = my_tuple + (' ',)
        try:
            my_tuple = my_tuple + (tweet['retweeted_status']['user']['screen_name'],)
        except:
            my_tuple = my_tuple + (' ',)
        #print my_tuple
        output_tuples.append(my_tuple)

    with open('02-07.csv', 'wb') as mycsvfile:
		thedatawriter = csv.writer(mycsvfile, delimiter=',')
		for row in output_tuples:
			thedatawriter.writerow(row)


if __name__ == '__main__':
    main(sys.argv[1:])
