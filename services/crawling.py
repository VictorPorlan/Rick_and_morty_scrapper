from urllib.request import urlopen
seed= 'https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html'
page = urlopen(seed)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
def convertir_string(pagina):
    page = urlopen(pagina)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def localizar_links(html_index):
    start_link= html_index.find('a href=')
    if start_link == -1:
        return None, 0
    start_quote= html_index.find("'", start_link)
    end_quote= html_index.find("'", start_quote + 1)
    url = html_index[start_quote+1 : end_quote]
    return url, end_quote

def por_crawlear(tocrawl, links):
    for link in links:
        if link not in tocrawl:
            tocrawl.append(link)
    return tocrawl

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

def crawl_web (seed):
    tocrawl =[seed]
    crawled =[]
    while tocrawl:
        pagina = tocrawl.pop()
        if pagina not in crawled:
            tocrawl = por_crawlear(tocrawl, conseguir_links(convertir_string(pagina)))
            crawled.append(pagina)
    return crawled
print(crawl_web(html))
        
        
            