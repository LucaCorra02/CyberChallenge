import requests
from bs4 import BeautifulSoup

def parseLink(link):
    return str(link).split('"')[1]

def addPageToVisit(visited,links):
    for link in links:
        keyPage = parseLink(link)    
        visited.append(keyPage)

def isFlag(text):
    if "{" in text:
        return True
    return False

def htmlUrl(url):
    resHtml = requests.get(url)
    return BeautifulSoup(resHtml.text,'html.parser')
  
def main():
    baseUrl = "http://web-16.challs.olicyber.it"
    flag=""
    toVisit = []
    visited = {}
   
    soap = htmlUrl(baseUrl)
    links = soap.find_all('a')
    addPageToVisit(toVisit,links)

    for page in toVisit:
        if page not in visited:
            visited[page] = True
            soap = htmlUrl(baseUrl+page)
            title = soap.find_all('h1')[0]
            print("Visiting page:",title)
            if isFlag(str(title)): 
                flag = title
                break
            addPageToVisit(toVisit,soap.find_all('a'))

    print("Flag: ",flag)


main()