from src.crawling import localizar_links, conseguir_links

def localizar_paquetes(html):
        conseguir_links(html)
        for enlace in links: