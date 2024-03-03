import requests
from bs4 import BeautifulSoup
from bs4 import Comment 

"""_summary_
La flag di questa challenge è in un commento della pagina web accessibile tramite l'indirizzo http://web-14.challs.olicyber.it/. 
L'obiettivo è estrarre e visualizzare i commenti contenuti nella pagina. Proprio come il browser, anche BeautifulSoup tende a mettere il contenuto dei commenti in secondo piano, non fornendo strumenti diretti di accesso ad essi. 
Si consiglia di utilizzare il parametro string del metodo find_all con un test personalizzato che verifichi se l'elemento analizzato sia un'istanza della classe Comment
"""

resHtml = requests.get("http://web-14.challs.olicyber.it/")
soap = BeautifulSoup(resHtml.text,'html.parser')
ris = soap.find_all(string=lambda text: isinstance(text, Comment))
print(ris[1])