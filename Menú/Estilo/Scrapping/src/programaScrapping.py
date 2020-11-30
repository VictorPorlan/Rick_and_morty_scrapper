from urllib.request import urlopen
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
principio = html.find("pack>")
final = html.find ("<")
nombre = html[principio + 1 : final]
print (nombre)