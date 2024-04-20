import numpy
import pandas
import pymongo
import  motor

from pymongo import MongoClient

### ither format is acceptable

#my_client = MongoClient("localhost", 27017)
my_client = MongoClient("mongodb://localhost:27017")
print(my_client)

#list databases
print(my_client.list_database_names())

#connect to test database
db = my_client.test
db = my_client["test"]
print(db)

#list collection names
print(db.list_collection_names())

#access a collection within the database

mtc = db['my_test_collection']
print(mtc)

####  CRUD

#Create

mtc.insert_one({"name": "Seema Archana", "job": "Software Engineer", "age": 34})
new_user = {
    "name": "Pradeep",
    "job": "Principal PM",
    "age": 43
}
mtc.insert_one(new_user)

#Read


