def crear_stock(html):
    inicio_stock = html.find("'stock'")
    marca_inicial_stock = html.find(':', inicio_stock)
    marca_final_stock = html.find('<', marca_inicial_stock)
    stock= html[marca_inicial_stock+2: marca_final_stock]
    return stock, marca_final_stock