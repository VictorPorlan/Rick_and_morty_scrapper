from src.crear_stock import crear_stock
def test_stock():
    assert crear_stock("<li class='stock'>Stock: 28<li>") == ('28',27)
def test_stock_dos():
    assert crear_stock("<li class='stock'>Stock: 136<li>") == ('136',28)