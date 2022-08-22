import requests
from bs4 import BeautifulSoup

class Search:
    """
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    
    t = soup.find("p",class_="location")
    w = soup.find_all("p",class_="location")
    for i in w:
        print(i.text)
    """


    def search(item):
        PHONE = "https://thatsthem.com/phone/" + item[0]
        EMAIL = "https://thatsthem.com/email/"+item[1]
        IP = "https://thatsthem.com/ip/"+item[2]
        VIN = "https://thatsthem.com/vin/"+item[3]

        pagePhone = requests.get(PHONE)
        pageEmail = requests.get(EMAIL)
        pageIP = requests.get(IP)
        pageVIN = requests.get(VIN)
        
        soup = []
        soup = BeautifulSoup(pagePhone.content, "html.parser")
        #soup = BeautifulSoup(pageEmail.content, "html.parser")
        #soup = BeautifulSoup(pageIP.content, "html.parser")
        #soup = BeautifulSoup(pageVIN.content, "html.parser")
        print(soup)
        w = soup.find_all("p",class_="location")
        for i in w:
            print(i.text)
    
item = []
item = "9042458765"
Search.search(item)

def deviceInfo():
    link = ""
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)
    
    pass