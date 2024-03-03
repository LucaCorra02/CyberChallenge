import requests

"""
    L'obiettivo di questa challenge è ottenere la risorsa http://web-02.challs.olicyber.it/server-records specificando il parametro id con il valore flag. 
    Si consiglia di utilizzare la parola chiave params della funzione get illustrata nella challange precedente.
"""

val = {'id': 'flag'}
r = requests.get('http://web-02.challs.olicyber.it/server-records', params=val)
print("Flag: "+r.text)