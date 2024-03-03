import requests
from bs4 import BeautifulSoup 

"""_summary_
In questa challenge la flag è contenuta nel secondo paragrafo della pagina web accessibile all'URL http://web-12.challs.olicyber.it/. 
Si consiglia di scaricare la pagina come una normale risorsa tramite la funzione get della libreria requests, e il metodo find_all della libreria BeautifulSoup per ottenere l'elenco dei paragrafi in essa contenuti.
"""

url = "http://web-12.challs.olicyber.it/"
resHtml = requests.get(url)
soup = BeautifulSoup(resHtml.text, 'html.parser')
print("Flag:",soup.find_all('p')[1])