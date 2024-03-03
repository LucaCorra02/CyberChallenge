import requests
from bs4 import BeautifulSoup
import re

"""_summary_
 In questa challenge la flag è in una delle risorse esterne della pagina accessibile all'indirizzo http://web-15.challs.olicyber.it/. 
 L'obiettivo è utilizzare find_all e gli altri strumenti messi a disposizione da BeautifulSoup per costruire un elenco delle risorse esterne della pagina, si consiglia quindi di utilizzare la funzione get per scaricarle e di eseguirvi all'interno una ricerca testuale per la stringa flag{   
"""

resHtml = requests.get("http://web-15.challs.olicyber.it/")
soap = BeautifulSoup(resHtml.text,'html.parser')
flag = ""
for text in soap.find_all(['script','link']):
    file = str(text).split(" ")[1].split('"')[1]
    ris = requests.get("http://web-15.challs.olicyber.it"+file)
    match = re.findall(r"flag{.+}",ris.text)
    if(match):
       flag = match[0]
print(flag)
    
        