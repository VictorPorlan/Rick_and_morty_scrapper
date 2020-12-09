from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def convertir_string(pagina):
    page = urlopen(pagina)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html