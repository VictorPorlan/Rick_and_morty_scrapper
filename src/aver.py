from urllib.request import urlopen


url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")

def conseguir_nombre(html):
    marca_clase_nombre = html.find('class="nombre">')
    marca_final_nombre = html.find('<',marca_clase_nombre)
    nombre_pack = html[marca_clase_nombre +1:marca_final_nombre]
    return nombre_pack

print (conseguir_nombre(html_link))

