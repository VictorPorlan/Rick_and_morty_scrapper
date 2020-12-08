from services.crear_nombre import crear_nombre
def test_crear_nombre():
    assert crear_nombre("\"nombre\">Hello<") == ('Hello', 14)
    assert crear_nombre("\"nombre\">>Holatest<") == ('>Holatest', 18)
    assert crear_nombre("\"nombre\"holaholahola>Pack Buenos Días</h2>") == ('Pack Buenos Días', 37)
    assert crear_nombre("<h2 class=\"nombre\">Pack Morty Style</h2>") == ('Pack Morty Style', 35)
    assert crear_nombre("\"nombre\"estoNoLoTieneQueDetectar><") == ('', 33)
    assert crear_nombre("><\"nombre\">Esto lo detecta!<") == ('Esto lo detecta!', 27)



