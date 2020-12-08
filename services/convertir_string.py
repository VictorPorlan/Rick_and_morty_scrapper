from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def convertir_string(pagina):
    page = urlopen(pagina)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    try:
        response = urlopen(pagina)
    except HTTPError as e:
        print('Código de error: ', e.code)
    except URLError as e:
        print('Razón error URL: ', e.reason)
    finally:
        print('Algo ha ido mal')
    return html