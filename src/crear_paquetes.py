from crear_objeto import crear_objeto
import pymongo
from pymongo import MongoClient

cluster= MongoClient("mongodb+srv://diciembre:proyectodediciembre@proyectodiciembre.gvt0s.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["Scrapping"]
collection = db["packs"]
def crear_paquetes(html):
        pack = {}
        inicio_pack = html.find('nombre')
        marca_inicial_nombre = html.find('>', inicio_pack)
        marca_final_nombre = html.find('<', marca_inicial_nombre)
        nombre = html[marca_inicial_nombre+1:marca_final_nombre]

        pack['Nombre pack'] = nombre
        html = html[marca_final_nombre:]
        inicio_calidad = html.find("calidad")
        marca_inicial_calidad= html.find('>',inicio_calidad)
        marca_final_calidad= html.find('<',marca_inicial_calidad)
        calidad = html[marca_inicial_calidad+1:marca_final_calidad]
        pack['calidad'] = calidad

        inicio_dimensiones = html.find('altura')
        marca_inicial_altura = html.find(':',inicio_dimensiones)
        marca_final_altura = html.find('<',inicio_dimensiones)
        altura = html[marca_inicial_altura+2 : marca_final_altura]
        inicio_ancho = html.find('ancho')
        marca_inicial_ancho = html.find(':',inicio_ancho)
        marca_final_ancho = html.find('<',inicio_ancho)
        ancho = html[marca_inicial_ancho+2 : marca_final_ancho]

        pack['dimensiones'] = {'altura':altura, 'ancho':ancho}
        
        html = html[marca_final_ancho:]
        carac, html, nombre_pack = crear_objeto(html)
        final_pack = html.find('/div')
        final_caracteristicas = html.find('section')
        pack[nombre_pack]=carac
        while final_pack > final_caracteristicas:
                carac, html, nombre_pack = crear_objeto(html)
                pack[nombre_pack] = carac
                final_caracteristicas = html.find('section')
                final_pack = html.find('/div')
                if final_caracteristicas == -1:
                        break
        collection.insert_one(pack)
        return pack,html
