#!/usr/bin/python

import os
import ast
import json
import sys
from pymongo import MongoClient

def main(argv):
    collect_name = str(argv[0]) + "_datamine"
    print "\tCollection name:", collect_name
    client = MongoClient()
    db = client.test_database
    data = getattr(db, collect_name)
    data.delete_many({})

    if(len(argv) > 1):
        collect2_name = str(argv[1]) + "_datamine"
        print "\tCollection name:", collect2_name
        data_large = getattr(db, collect2_name)


    iMonth = int(argv[0][:2])
    iDay = int(argv[0][3:])
    directory = "/./" + str(iMonth) + "/" + str(iDay) + "/"
    count = 0
    for filename in os.listdir(directory):
        with open(directory + filename) as f:
            text_string = f.read()
            my_json = ast.literal_eval(text_string)
            data.insert_one(my_json)

            if(len(argv) > 1):
                data_large.insert_one(my_json)

        count += 1

if __name__ == '__main__':
    main(sys.argv[1:])
