import requests
from bs4 import BeautifulSoup
import re

resHtml = requests.get("http://web-15.challs.olicyber.it/")
soap = BeautifulSoup(resHtml.text,'html.parser')
flag = ""
for text in soap.find_all(['script','link']):
    file = str(text).split(" ")[1].split('"')[1]
    ris = requests.get("http://web-15.challs.olicyber.it"+file)
    match = re.findall(r"flag{.+}",ris.text)
    if(match):
       flag = match[0]
print(flag)
    
        