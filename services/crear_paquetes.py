from crear_nombre import crear_nombre
from crear_calidad import crear_calidad
from crear_precio import crear_precio
from crear_stock import crear_stock
from crear_dimensiones import crear_dimensiones
from crear_contenidos import crear_contenidos
from crear_objeto import crear_objeto
import pymongo
from pymongo import MongoClient

cluster= MongoClient("mongodb+srv://diciembre:proyectodediciembre@proyectodiciembre.gvt0s.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["Scrapping"]
collection = db["packs"]
def crear_paquetes(html):
        pack = {}
        nombre, marca_final_nombre = crear_nombre(html)
        pack['Nombre pack'] = nombre
        html = html[marca_final_nombre:]
        calidad, marca_final_calidad = crear_calidad(html)
        pack['calidad'] = calidad
        html = html[marca_final_calidad:]
        precio, marca_final_precio = crear_precio(html)
        pack['precio'] = precio
        html= html[marca_final_precio:]
        stock, marca_final_stock = crear_stock(html)
        pack['stock'] = stock
        altura, ancho, marca_final_ancho = crear_dimensiones(html)
        pack['dimensiones'] = {'altura':altura, 'ancho':ancho}
        html = html[marca_final_ancho:]
        contenidos, html = crear_contenidos(html)
        pack['contenidos'] = contenidos
        collection.insert_one(pack)

        return pack,html
        
        