import requests

"""
L'obiettivo di questa challenge è ottenere il testo della risorsa radice del server web-01.challs.olicyber.it, identificata dall'URL http://web-01.challs.olicyber.it/
Si consiglia di utilizzare la funzione get della libreria requests.
"""

r = requests.get('http://web-01.challs.olicyber.it/')
print(r.text)