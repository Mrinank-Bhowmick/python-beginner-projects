import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["Mongo"]
