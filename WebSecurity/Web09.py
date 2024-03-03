import requests

"""_summary_
Analogamente alla precedente, l'obiettivo di questa challenge è inviare una richiesta POST verso la risorsa http://web-09.challs.olicyber.it/login fornendo in formato JSON la coppia di valori "username": "admin" e "password": "admin", analogamente a un'ipotetica operazione di login nei confronti di un servizio web.
 La flag sarà restituita nel testo della risposta all'operazione.
"""

url = "http://web-09.challs.olicyber.it/login"
toParse = {'username':'admin', 'password':'admin'} 
response = requests.post(url, json=toParse) ##oppure json.dumps(dict)
print("Flag: ",response.json()["token"])

