from src.crear_calidad import crear_calidad
def test_calidad():
    assert crear_calidad("\"patata\">Basic<") == ('"patata">Basic', 14)
    assert crear_calidad("\"calidad\"><") == ('', 10)
    assert crear_calidad("<li class='calidad'>Basic</li>") == ('Basic',25)
    assert crear_calidad("<li class='calidad'>Basic</li><li class='precio'>Precio: 10€</li><li class='stock'>Stock: 158</li><ul><li class='calidad'>Basic</li>") == ('Basic',25)
    assert crear_calidad(">Pack Rick Style </h2><ul><li class='calidad'>Premium<li><li class='precio'>Precio: 30€</li><li class='stock'>Stock: 35<li>") == ('Premium', 53)
    assert crear_calidad(">Pack Rfaafafdli class='calidad'>Buñueloasdfg<li><li class='precio'>Precio: 30€</li><li class='stock'>Stock: 35<li>") == ('Buñueloasdfg', 45)
    assert crear_calidad("\"calidad\">Basic<") == ('Basic', 15)
