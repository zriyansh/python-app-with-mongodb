#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the MongoClient class
import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors

load_dotenv()

DOMAIN = os.getenv("DOMAIN")

# global variables for MongoDB host (default port is 27017)
# DOMAIN = '72.17.0.2'
# DOMAIN = '10.0.41.209'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        host = [ str(DOMAIN) + ":" + str(PORT) ],
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = "objectrocket",
        password = "1234",
        # password = "WPesOBOB3P",
    )

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])

    # get the database_names from the MongoClient()
    database_names = client.list_database_names()

except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    client = None
    database_names = []

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)

print ("\ndatabases:", database_names)