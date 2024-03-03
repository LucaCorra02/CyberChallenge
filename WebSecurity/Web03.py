import requests

"""
In questa challenge, uno header non-standard è stato usato per fornire un meccanismo di autenticazione artigianale. 
L'obiettivo è ottenere il testo della risorsa all'indirizzo http://web-03.challs.olicyber.it/flag, ma il server risponderà solo a richieste che conterranno lo header X-Password contenente la password corretta, admin.
Si consiglia di utilizzare la parola chiave headers della funzione get utilizzata nelle challenge precedenti.
"""

pers = {"X-Password":"admin"}
r = requests.get("http://web-03.challs.olicyber.it/flag", headers=pers)
print("Flag: "+r.text)