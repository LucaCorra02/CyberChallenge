import requests

"""_summary_
L'obiettivo di questa challenge è eseguire una richiesta HEAD alla risorsa http://web-07.challs.olicyber.it/ ed osservare gli header restituiti. 
Si consiglia di utilizzare la funzione head della libreria requests, di utilizzo analogo a quello della funzione get.
"""
url = "http://web-07.challs.olicyber.it/"
r = requests.head(url)
print("Flag: "+r.headers['X-Flag'])