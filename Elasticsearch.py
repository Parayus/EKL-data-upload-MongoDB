import pymongo
from bson.objectid import ObjectId
from pprint import pprint
import requests, json, os
import elasticsearch
import datetime


myclient = pymongo.MongoClient("mongodb://kettleusrmongo:k3Tt13U53rPr06m0n0g0@uat.kettle.chaayos.com:27017/admin?authSource=admin&connectTimeoutMS=300000")
mydb = myclient["kettle_analytics"]
mycol = mydb["wsCrashLog"]

es = Elasticsearch([{"host":"localhost","port":9200}])
if es.indices.exists(index="crashlog"):
    startTime = es.search(index="crashlog", doc_type="ws", body = {
    '_source' : ["uploadTime"],
    'size' : 1,
    'sort': { "_id": "desc"},
    'query': {
    'match_all' : {}
    }
    })   # get last uploaded doc from index and fetch its uploadTime
    myquery = {"uploadTime" : {"$gt":startTime}} #query to fetch latest data
    all_objects = mycol.find(myquery).sort('uploadTime') #fetches latest data
else:
    all_objects = mycol.find().sort('uploadTime')



allObjects = []


for x in all_objects:
    allObjects.append(x)



for i in range(len(allObjects)):
    allObjects[i]["uploadTime"] = str(allObjects[i]["uploadTime"])
    allObjects[i]["_id"] = str(allObjects[i]["_id"])
    allObjects[i]["id"] = str(allObjects[i]["_id"])
    del allObjects[i]["_id"]                        # deleting '_id' key as its collides with in built id of elasticsearch key



for j in range(len(allObjects)):
    json_all = json.dumps(allObjects[j])
    time = datetime.datetime.now()
    es.index(index="crashlog",doc_type="ws",id=time, body=json_all)

