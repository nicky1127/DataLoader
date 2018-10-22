#import
from pymongo import MongoClient
from bson.objectid import ObjectId

#connection
conn=MongoClient("mongodb://localhost:27017/")
print(conn.list_database_names())
#2 way
db=conn.test
print(db.list_collection_names())
#db=conn["users"]

collection=db.users
#collection=db["users"]

#print(collection.stats)
#results=collection.insert_many([{"Name":'yes1'},{"Name":'No1'}])
#print(results.inserted_ids)
result=collection.insert_one({"Name":"No1"}).inserted_id
print(result)
cursor = collection.find()
for data in cursor:
    print(data)