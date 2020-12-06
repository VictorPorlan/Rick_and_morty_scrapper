import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId
cluster="mongodb+srv://diciembre:proyectodediciembre@proyectodiciembre.gvt0s.mongodb.net/<dbname>?retryWrites=true&w=majority"
db = cluster["Scrapping"]
collection = db["packs"]

#user: diciembre
#password: proyectodediciembre
client= pymongo.MongoClient(uri)
try:
    return pymongo.MongoClient()
    except pymongo.errors.ConnectionFailure
    print ("La conexión ha fallado")
    except:
    print("Algo no ha salido bien")
    finally:
    print("Ya se ha hecho el  try except")

subir_base = client.sample_proyecto
coleccion = proyecto.packs_amenities
coleccion.drop()

result = packs.insert_many(#eldiccionario)

####try:
#x = 'spam'[99]
#except IndexError:
#print('except run')
#finally:
#print('finally run')
#print('after run')
#print(sep + 'NO EXCEPTION RAISED')
#try:
#x = 'spam'[3]
#except IndexError:
#print('except run')
#finally:
#print('finally run')
#print('after run')
##print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
#try:
#x = 'spam'[3]
#except IndexError:
#print('except run')
#else:

#Unified try/except/finally | 1105

#www.it-ebooks.info

#print('else run')
#finally:
#print('finally run')
#print('after run')
#print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
##try:
#x = 1 / 0
#except IndexError:
#print('except run')
#finally:
#print('finally run')
#print('after run')