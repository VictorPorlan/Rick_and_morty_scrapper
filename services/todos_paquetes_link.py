from crear_paquetes import crear_paquetes

def todos_paquetes_link (html):
    paquetes = []
    nombre = html.find('nombre')
    while nombre != -1:
        pack, html = crear_paquetes(html)
        paquetes.append(pack)
        nombre = html.find('nombre')
    return paquetes