import requests

"""_summary_
L'obiettivo di questa challenge è eseguire una richiesta GET alla risorsa http://web-06.challs.olicyber.it/token che cercherà di installare un cookie di sessione, una volta ottenuto il quale sarà possibile accedere a http://web-06.challs.olicyber.it/flag per ottenere la flag.
La funzione get della libreria requests usata finora adotta un modello senza stato, ovvero non utilizza nessuna delle informazioni precedentemente ricevute dal server nella composizione delle richieste successive. 
Per completare questa challenge, si consiglia di istanziare un oggetto di classe Session ed eseguire le richieste tramite il suo metodo get, che differisce dalla normale funzione get proprio per la caratteristica di salvare queste informazioni all'interno dell'oggetto emulando parzialmente il comportamento un browser.
"""

session = requests.Session()

session.get('http://web-06.challs.olicyber.it/token')
ris = session.get("http://web-06.challs.olicyber.it/flag") ##invia in automatico il cookie al server
print("Flag: ",ris.text)
