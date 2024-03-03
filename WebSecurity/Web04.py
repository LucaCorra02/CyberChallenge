import requests

"""
L'obiettivo di questa challenge è richiedere la risorsa http://web-04.challs.olicyber.it/users utilizzando la rappresentazione alternativa application/xml anziché quella di default application/json.
Si consiglia di provare ad ottenere la risorsa normalmente, e successivamente specificando un tipo di rappresentazione diversa (application/xml) tramite lo header Accept.
"""

head = {"Accept":"application/xml"}
richiesta = requests.get("http://web-04.challs.olicyber.it/users",headers=head)
print(richiesta.text)