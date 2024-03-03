import requests
from bs4 import BeautifulSoup 

url = "http://web-12.challs.olicyber.it/"
resHtml = requests.get(url)
soup = BeautifulSoup(resHtml.text, 'html.parser')
print("Flag:",soup.find_all('p')[1])