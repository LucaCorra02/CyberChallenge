import requests
from bs4 import BeautifulSoup 
import re

"""_summary_
    In questa challenge le lettere evidenziate nella pagina web accessibile all'URL http://web-13.challs.olicyber.it/ formano la flag. 
    L'obiettivo è isolarle dal resto della pagina e concatenarle. 
    Si consiglia di utilizzare il metodo find_all della libreria BeautifulSoup con un filtro adeguato, e di iterare sul risultato.
"""

resHtml = requests.get("http://web-13.challs.olicyber.it/")
soap = BeautifulSoup(resHtml.text,'html.parser')
flag = ""
for text in soap.find_all(class_='red'):
    flag+=re.split(r'>|<',str(text))[2]
print("flag{"+flag+"}")