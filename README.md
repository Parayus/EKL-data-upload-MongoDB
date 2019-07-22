# EKL-data-upload-MongoDB
Objective - To create a Analytical Dashboard with help from Elasticsearch and Kibana importing data from MongoDB 
Imports-import pymongo
        from bson.objectid import ObjectId
        from pprint import pprint
        import requests, json, os
        from elasticsearch import Elasticsearch
        from elasticsearch import helpers
Import data from MongoDB- Use mongo client to connect to read data from your data base and save it in a object.

Intersetingly the type of the object created will be <class 'pymongo.cursor.Cursor'> in order to get it uploaded on elasticsearch we need to convert its type to json.

Converting object to Json - Inorder this to happen the data set should be of type dict and all objects inside it should be of                             kind string so check the type of each key value in object inorder to save time and convert all of                             them to string.Then use json.dump() to change it to json
Uploading Data to elasticsearch - To keep '_id' unique of the uploading data we used timestamp to solve the problem.

Our current solution is good for small database.
As database at whcih I was working is a growing database I need to import only new data that occured on my database.
Inorder to solve the above mentioned problem I got the uploadtime of the latest uploaded data in order to compare the uploadtime of data present in database and fetch new data only. 
This saves memory and processing as database will grow bigger.

Note- If a key name '_id' exists change its key name as it wil return error as it collides with '_id' of elasticsearch 

Finally,use kibana to analyse your data.
