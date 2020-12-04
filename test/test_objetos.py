from src.scrapping import crear_objeto, html_index, crear_caracteristicas

def rifle_pulso(hmtl):
    assert crear_objeto(html[1300:]) == {'nombre': 'Rifle de pulso ', 'caracteristicas': {'Color': 'multicolor', 'Cantidad': '3', 'Material': 'Cadmio', 'Calidad': 'Más o menos'}}
