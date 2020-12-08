from src.crawl_web import crawl_web
from src.todos_paquetes_link import todos_paquetes_link
from urllib.request import urlopen
link = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"

def web_scrapping (link):
    lista = []
    links = crawl_web(link)
    for enlace in links:
        packs_de_un_link = []
        url = enlace
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        buscador = html.find('nombre')
        if buscador != -1:
            packs_de_un_link = todos_paquetes_link(html)
            lista.append(packs_de_un_link)
    return lista
print(web_scrapping(link))

