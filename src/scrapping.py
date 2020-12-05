from urllib.request import urlopen
from crear_paquetes import crear_paquetes
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")

def scrapping (html):
    paquetes = []
    while html.find('nombre') != -1:
        pack, html = crear_paquetes(html)
        paquetes.append(pack)
    return paquetes

print(scrapping(html_link))