from crawling import conseguir_links
from scrapping import scrapping
from urllib.request import urlopen
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"
page = urlopen(url)
html_bytes = page.read()
html_index = html_bytes.decode("utf-8")
def web_scrapping (html_index):
    lista = []
    links = conseguir_links(html_index)
    for enlace in links:
        packs_de_un_link = []
        url = enlace
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        buscador = html.find('nombre')
        if buscador != -1:
            packs_de_un_link = scrapping(html)
            lista.append(packs_de_un_link)
            
    return lista
print(web_scrapping(html_index))

