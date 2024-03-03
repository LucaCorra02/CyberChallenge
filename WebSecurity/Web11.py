import requests

"""
In questa challenge, la flag è divisa in quattro pezzi, accessibili tramite la risorsa http://web-11.challs.olicyber.it/flag_piece in base al parametro index. Per accedervi, è necessario aver precedentemente inviato una richiesta POST di login alla risorsa http://web-11.challs.olicyber.it/login, con body JSON contenente "username": "admin" e "password": "admin", e aver ricevuto in cambio un cookie di sessione. 
Oltre al token di sessione nel cookie, la risorsa login restituirà anche un token CSRF nel corpo della risposta (anch'esso JSON).
Ad ogni richiesta correttamente eseguita il client riceverà un nuovo token da utilizzare per la successiva.
"""
session = requests.Session()

def login(url,user,psw) :
    credential={"username":user,"password":psw}
    login = session.post(url,json=credential)
    return login.json()['csrf']

def flag(url,token,index):
    r = session.get(url, params={"csrf":token,"index":index})
    return r.json()['flag_piece']

def main():
    urlFlag = "http://web-11.challs.olicyber.it/flag_piece"
    urlLogin = "http://web-11.challs.olicyber.it/login"
    cr = "admin"
    ris = ""
    for i in range(0,100):
        ris += flag(urlFlag,login(urlLogin,cr,cr),i)
        if "}" in ris:
            break

    print(ris)

main()



