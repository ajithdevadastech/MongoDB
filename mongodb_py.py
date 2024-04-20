import numpy
import pandas
import pymongo
import  motor

from pymongo import MongoClient

my_client = MongoClient("localhost", 27017)
print(my_client)