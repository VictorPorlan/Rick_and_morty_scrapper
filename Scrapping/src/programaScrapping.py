from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
principio = html.find("Name:")
final = html.find ("<", principio)
Nombre = html[principio+6 : final]
print(Nombre)
