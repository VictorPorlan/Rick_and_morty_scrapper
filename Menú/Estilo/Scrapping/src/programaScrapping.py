from urllib.request import urlopen
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
def get_next_target(html):
    start_link= html.find('a href=')
    start_quote= html.find("'", start_link)
    end_quote= html.find("'", start_quote + 1)
    url = html[start_quote+1 : end_quote]
    return url, end_quote
def conseguir_links(html):
    links = []
    while True:
        url, endpos = get_next_target(html)
        if url:
            links.append(url)
            html=html[endpos:]
        else:
            break
    return links    
print(conseguir_links(html))
if __name__ == "__main__":
    assert conseguir_links(html) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html',]