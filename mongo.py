import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


new_doc = [{
           "firstname": "terry",
           "last": "pratchett",
           "dob": "11/03/1952",
           "gender": "m",
           "hair_color": "none",
           "occupation": "writer",
           "nationality": "british"
           }, {
           "firstname": "george",
           "last": "rr martin",
           "dob": "20/09/1948",
           "gender": "m",
           "hair_color": "grey",
           "occupation": "writer",
           "nationality": "american"}]

coll.insert_many(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
