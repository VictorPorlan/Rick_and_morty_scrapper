from services.crear_objeto import crear_objeto
def test_crear_objeto():
    assert crear_objeto("<ul><li class=\"objeto\"><h3>Peluche Pickle Rick</h3><ul class=\"lista\"> <section><li class=\"caracteristica\">Cantidad: 1</li><li class=\"caracteristica\">Material: algodon</li></section></ul>") == {'caracteristicas': {'Cantidad': '1', 'Material': 'algodon'}