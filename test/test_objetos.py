from services.crear_calidad import crear_calidad
def test_calidad():
    assert crear_calidad("<li class='calidad'>Basic</li>") == ('Basic',25)

