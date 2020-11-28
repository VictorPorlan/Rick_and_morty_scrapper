from urllib.request import urlopen
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")


def conseguir_links(html):
    links=[]
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            html=html[endps:]
            else:
                break
