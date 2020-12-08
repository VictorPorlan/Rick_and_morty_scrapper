from services.crawl_web import crawl_web
def test_links():
    assert crawl_web('https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html') == ['https://bertavr.github.io/Proyecto_Rick_y_Morty/premium.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/standard.html', 'https://bertavr.github.io/Proyecto_Rick_y_Morty/index.html']