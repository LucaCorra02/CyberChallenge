import requests
from bs4 import BeautifulSoup 
import re

resHtml = requests.get("http://web-13.challs.olicyber.it/")
soap = BeautifulSoup(resHtml.text,'html.parser')
flag = ""
for text in soap.find_all(class_='red'):
    flag+=re.split(r'>|<',str(text))[2]
print("flag{"+flag+"}")