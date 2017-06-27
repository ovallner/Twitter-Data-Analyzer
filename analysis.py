#!/usr/bin/python

import json
import csv
import string
import re
import sys
from wordcloud import WordCloud
from pymongo import MongoClient

def main(argv):

	collect_name = str(argv[0]) + "_datamine"
	client = MongoClient()
	db = client.test_database
	data = getattr(db, collect_name)


	tweets = data.find(no_cursor_timeout=True)
	tweet_list = []
	word_str = ""

	for twe in tweets:
		word_str += twe['text']
		tweet_list.append(twe['text'].lower())

	punctuation_list = []
	for char in string.punctuation:
		punctuation_list.append(char)

	# This list contains the words used to determine if a tweet is
	# Math or education related. To 
	math_ed_words = ["math", "maths", "education", "school", "schools", "student", "students", "learn", "teach", "teaching", "teacher", "professor", "taught", "grade",
					"tutor", "tutoring", "elementary", "lesson", "lecture", "kindergarten", "classroom", "class", "mathematical", "mathematics",
					"#mtbos", "mtbos", "#mathchat", "mathchat", "edtech", "#edtech", "edchat", "#edchat",
					"calculus", "calc", "algebra", "alg", "geometry", "precal", "precalc", "precalculus", "trig", "trigonometry",
					"addition", "subtraction", "multiplication", "division", "fraction", "fractions", "decimal", "decimals",
					"derivative", "integral", "equation", "quadratic", "product", "sum", "number", "numbers", "angle",]

	math_ed_tweets = 0
	for tweet in tweet_list:
		words = tweet.split()
		for word in words:
			if word in math_ed_words:
				math_ed_tweets += 1
				break


	print "\tTotal tweets: ", len(tweet_list)
	print "\tNumber of Tweets about math education: ", math_ed_tweets
	print "\tPercent of Tweets about math education: ", ( (float(math_ed_tweets)/len(tweet_list)) * 100 ), "%"

	word_list = word_str.split()
	word_str = ' '.join(i for i in word_list if i not in punctuation_list)

	# Generate a word cloud image
	wordcloud = WordCloud(max_font_size=40).generate(word_str)

	# Display the generated image:
	# the matplotlib way:
	import matplotlib.pyplot as plt
	plt.figure()
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
