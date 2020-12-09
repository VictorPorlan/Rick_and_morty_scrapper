from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def convertir_string(pagina):
    try:
        page = urlopen(pagina)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
    except:
        print('Algo ha fallado durante el request del HTML. Intentalo de nuevo')
    return html