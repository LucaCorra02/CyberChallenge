import requests

"""_summary_
  L'obiettivo di questa challenge è inviare una richiesta POST verso la risorsa http://web-08.challs.olicyber.it/login fornendo nel formato application/x-www-form-urlencoded la coppia di valori "username": "admin" e "password": "admin", analogamente a un'ipotetica operazione di invio di un form di login su un sito web. 
  La flag sarà restituita nel testo della risposta all'operazione.  
"""

url = "http://web-08.challs.olicyber.it/login"
cred = {"username": "admin","password": "admin"}
r = requests.post(url,data=cred)
print(r.text)