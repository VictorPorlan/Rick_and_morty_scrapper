from src.crawling import conseguir_links, html, get_next_target
def test_links():
    assert conseguir_links(html) == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html']