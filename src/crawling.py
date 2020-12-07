from urllib.request import urlopen

url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"
page = urlopen(url)
html_bytes = page.read()
html_index = html_bytes.decode("utf-8")


link_index_pagina = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"

def sacar_html(index): 
#esto es lo que saca html, lo he puesto en función para poder usarlo en el crawler y en el bucle sin estar copiando cada vez
    page = urlopen(index)
    html_bytes = page.read()
    html_index = html_bytes.decode("utf-8")
    assert isinstance(html_index, str)
    return html_index
assert isinstance(html_index, str)
#aquí hay que hacer un try pq podría fallar a la hora de sacar la página (y no depende de nuestro código)

def localizar_links(html_index):
    start_link= html_index.find('a href=')
    start_quote= html_index.find("'", start_link)
    end_quote= html_index.find("'", start_quote + 1)
    url = html_index[start_quote+1 : end_quote]
    return url, end_quote


def links_una_pagina(html):
    links = []
    while True:
        url, endpos = localizar_links(html)
        if url:
            links.append(url)
            html=html[endpos:]
        else:
            break
    return links  
    
    assert isinstance(links, list)
    assert len(links) == html.count('https')
            
def links_todo(pagina_raiz):
    por_crawlear = [pagina_raiz]
    crawleadas = []
    while por_crawlear:
        pagina = por_crawlear.pop()
        if pagina not in crawleadas:
            for elemento in localizar_links(sacar_html(pagina)):
                if elemento not in por_crawlear:
            por_crawlear.append(elemento)            
        crawleadas.append(pagina)
    return crawleadas
    print links_todo(link_index_pagina)
            


def sacar_html_todo(index): #esto es el bucle links
    lista_links =  link_todo(index)
    lista_codigos_fuente = []
    for enlace in lista_links:
        lista_codigos_fuente.append(sacar_html(enlace))
    assert len(lista_codigos_fuente) == len(links_todo(index))
    return  lista_codigos_fuente
print (crawl_conseguir_html(link_index_pagina)) #print que hay que quitar#



if __name__ == "__main__": 
    assert conseguir_links(link_index_pagina) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html']