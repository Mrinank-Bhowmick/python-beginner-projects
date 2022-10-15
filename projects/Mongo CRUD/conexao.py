import pymongo

# CONNECTION ON MONGO DB
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["Mongo"]
