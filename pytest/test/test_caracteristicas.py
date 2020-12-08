from src.crear_caracteristicas import crear_caracteristicas

def test_cuatro_caracteristicas():
    assert crear_caracteristicas('<section><li class="caracteristica ">Color: Negro</li><li class="caracteristica ">Cantidad: 1</li><li class="caracteristica ">Material: Nylon</li><li class="caracteristica ">Calidad: Funciona cuando quiere</li></section>') == ({'Color': 'Negro', 'Cantidad': '1', 'Material': 'Nylon', 'Calidad': 'Funciona cuando quiere'}, 'ction>')

def test_tres_caracteristicas():
    assert crear_caracteristicas('<ul class="lista "><section><li class="caracteristica ">Color: Verde</li><li class="caracteristica ">Cantidad: 1</li><li class="caracteristica ">Material: Cadmio</li><li class="caracteristica ">Calidad: Decente</li></section>') == ({'Color': 'Verde', 'Cantidad': '1', 'Material': 'Cadmio', 'Calidad': 'Decente'}, 'ction>')

def test_dos_caracteristicas():
    assert crear_caracteristicas('<ul class="lista "><section><li class="caracteristica ">Color: Rojo</li><li class="caracteristica ">Calidad: Buena</li></section></ul>') == ({'Color': 'Rojo', 'Calidad': 'Buena'}, 'ction></ul>')

def test_una_caracteristica():
    assert crear_caracteristicas('<ul class="lista "><section><li class="caracteristica ">Calidad: Decente</li></section>') == ({'Calidad': 'Decente'}, 'ction>')
