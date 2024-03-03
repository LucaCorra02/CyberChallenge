import requests
"""
    In maniera simile alla challenge numero 3, l'obiettivo è ottenere la risorsa http://web-05.challs.olicyber.it/flag fornendo la stringa admin in un cookie di nome password. 
    Si consiglia di utilizzare il parametro cookies della funzione get utilizzata fino a questo momento.
"""
cookies = {"password":"admin"}
r = requests.get("http://web-05.challs.olicyber.it/flag", cookies=cookies)
print("Flag: "+r.text)