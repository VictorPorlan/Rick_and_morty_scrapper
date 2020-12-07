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

def unir_lista(por_crawlear , links_pagina_nueva):
    for elemento in links_pagina_nueva:
        if elemento not in por_crawlear:
            por_crawlear.append(elemento)

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
            unir_lista(por_crawlear, links_una_pagina(sacar_html(pagina))
            crawleadas.append(pagina)
    return crawleadas
    print links_todo(link_index_pagina)
            


if __name__ == "__main__": 
    assert conseguir_links(link_index_pagina) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html']