from urllib.request import urlopen
url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html"
page = urlopen(url)
html_bytes = page.read()
html_index = html_bytes.decode("utf-8")

assert isinstance(html_index, str)

def localizar_links(html_index):
    start_link= html_index.find('a href=')
    start_quote= html_index.find("'", start_link)
    end_quote= html_index.find("'", start_quote + 1)
    url = html_index[start_quote+1 : end_quote]
    return url, end_quote

def conseguir_links(html):
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
print(conseguir_links(html_index))
            
        
        
            