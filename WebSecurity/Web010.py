import requests

"""_summary_
L'obiettivo di questa challenge è determinare l'insieme dei verbi supportati per la risorsa http://web-10.challs.olicyber.it/, provare a utilizzarne uno poco comune e imprevisto ed osservare la risposta. 
La libreria requests mette a disposizione funzioni analoghe alla funzione get anche per i verbi meno comuni, come put e patch.  
"""

url = "http://web-10.challs.olicyber.it/"
verbi = requests.options(url)
print(verbi.headers['Allow'])
response1 = requests.put("http://web-10.challs.olicyber.it/")
print("Flag: ",response1.headers['X-Flag'])