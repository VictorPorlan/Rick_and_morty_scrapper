import nltk
from urllib import urlopen
url = "../Indice/Index.html"
html = urllib.urlopen(url).read()
raw = nltk.clean_html(html)  
print(raw)



