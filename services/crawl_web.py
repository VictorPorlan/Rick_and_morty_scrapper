from services.conseguir_links import conseguir_links
from services.convertir_string import convertir_string
def crawl_web (seed):
    tocrawl =[seed]
    crawled =[]
    while tocrawl:
        pagina = tocrawl.pop()
        if pagina not in crawled:
            links = conseguir_links(convertir_string(pagina))
            tocrawl = tocrawl + links
            crawled.append(pagina)
    return crawled