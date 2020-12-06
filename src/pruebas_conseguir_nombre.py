import pymongo
from pymongo import MongoClient

cluster= MongoClient("mongodb+srv://diciembre:proyectodediciembre@proyectodiciembre.gvt0s.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["Scrapping"]
collection = db["packs"]

prueba = {"name": "rick", "pack": "premium"}

collection.insert_one(prueba)

