from urllib.request import urlopen

link_index_pagina = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"

def sacar_html(index): 
#esto es lo que saca html, lo he puesto en función para poder usarlo en el crawler y en el bucle sin estar copiando cada vez
    page = urlopen(index)
    html_bytes = page.read()
    html_index = html_bytes.decode("utf-8")
    assert isinstance(html_index, str)
    return html_index


def conseguir_links(index):
#esto es el crawler
    html_index = sacar_html(index)
    lista_links = []
    while html_index.find('a href') != -1: #el while comprueba que haya a href (ya que al final del bucle corto el html)
        inicio_link = html_index.find("a href='") + len("a href='")  #busca la posición de después de a href=' 
        final_link = html_index.find("'>", inicio_link)  #busca la posición donde acaba el link ('>)
        link = html_index[inicio_link : final_link] #saca el códifo desde la posición de después del a href hasta la posicion del('>) o sea el link
        lista_links.append(link) 
        html_index = html_index[final_link : ] #corta el html como habías hecho tú
    assert isinstance(lista_links, list)
    assert len(lista_links) == sacar_html(index).count('https') ###esta aserción habría que quitarla o refactorizarla si eventualmente se añadieran urls con otro formato (caso hipotético)
    return lista_links

    print (conseguir_links(link_index_pagina)) #print que hay que quitar#

def crawl_conseguir_html(index): #esto es el bucle links
    lista_links =  conseguir_links(index)
    lista_codigos_fuente = []
    for enlace in lista_links:
        lista_codigos_fuente.append(sacar_html(enlace))
    assert len(lista_codigos_fuente) == len(conseguir_links(index))
    return  lista_codigos_fuente
print (crawl_conseguir_html(link_index_pagina)) #print que hay que quitar#
if __name__ == "__main__": 
    assert conseguir_links(link_index_pagina) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html']
    #ahora los links son solo 3 (el de indice no está, pero ahí tampoco se scrapeaba nada) 
    # porque he quitado el menu del indice, y he puesto los links en imágenes, pero funciona :D 