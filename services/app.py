from crawl_web import crawl_web
from todos_paquetes_link import todos_paquetes_link
from convertir_string import convertir_string
from urllib.request import urlopen
import pymongo
from pymongo import MongoClient
import sys
cluster= MongoClient("mongodb+srv://diciembre:proyectodediciembre@proyectodiciembre.gvt0s.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["Scrapping"]
collection = db["packs"]

link = "https://victorporlan.github.io/Rick_and_morty_scrapper/index.html"
def web_scrapping (link):
    try:
        collection.drop()
    except:
        sys.exit('No se ha podido reiniciar la colección. Intentalo de nuevo.')
    lista = []
    links = crawl_web(link)
    for enlace in links:
        html = convertir_string(enlace)
        buscador = html.find('nombre')
        if buscador != -1:
            packs_de_un_link = todos_paquetes_link(html)
            lista.append(packs_de_un_link)
    return lista
print(web_scrapping(link))

