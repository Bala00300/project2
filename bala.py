from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class flipkart:
    httpObject = urlopen(
        "https://www.flipkart.com/search?q=laptop+8gb%2F1tb&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=laptop+8gb%2F1tb%7CLaptops&requestId=1855a144-3239-4797-947e-89d46192ace1&as-searchtext=laptop+8&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5")
    webdata = httpObject.read()
    soupdata = soup(webdata, 'html.parser')

    httpObject1 = urlopen("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.network_type%255B%255D%3D4G&p%5B%5D=facets.network_type%255B%255D%3D4G%2BVOLTE&p%5B%5D=facets.ram%255B%255D%3D6%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB")
    webdata1 = httpObject1.read()
    soupdata1 = soup(webdata1, 'html.parser')

    def laptop(self):
        containers = self.soupdata.findAll('div', {'class': '_2kHMtA'})

        f = open('laptop_info.csv', 'wb')
        f.write("BrandName,Price,Processor,Ram,Storage\n".encode())
        for container in containers:
            Brand = container.find('div', {'class': '_4rR01T'})
            BrandName = Brand.text.split('_')[0].strip()
            Price = container.find('div', {'class': '_30jeq3 _1_WHN1'}).text.replace(',', '').replace('₹', '')
            info = container.findAll('li', {'class': 'rgWa7D'})
            Processor = info[0].text
            Ram = info[1].text
            Storage = info[3].text
            f.write(f"{BrandName},{Price},{Processor},{Ram},{Storage}\n".encode())
        f.close()

        df = pd.read_csv('laptop_info.csv')

        Top5 = df.sort_values(by='Price', ascending=True).head(5)
        Top5.to_csv('out.csv')
        print(Top5)

        plt.figure(figsize=(15, 7))
        plt.bar(x=Top5['BrandName'], height=Top5['Price'])
        plt.title('Lowest priced laptop', fontsize=30)
        plt.xlabel('BrandName', fontsize=15)
        plt.ylabel('Price', fontsize=15)
        plt.xticks(rotation=270)
        plt.savefig('top5.jpg')
        plt.show()

    def mobile(self):
        CONTAINERS = self.soupdata1.findAll('div', {'class': '_2kHMtA'})

        f = open('mobile_info.csv', 'wb')
        f.write("Brandname,price,RamRomMemory\n".encode())
        for CONTAINER in CONTAINERS:
            brand = CONTAINER.find('div', {'class': '_4rR01T'})
            Brandname = brand.text
            price = CONTAINER.find('div', {'class': '_30jeq3 _1_WHN1'}).text.replace(',', '').replace('₹', '')
            info = CONTAINER.findAll('li', {'class': 'rgWa7D'})
            RamRomMemory= info[0].text

            f.write(f"{Brandname},{price},{RamRomMemory}\n".encode())
        f.close()

        df = pd.read_csv('mobile_info.csv')

        top5 = df.sort_values(by='price', ascending=True).head(5)
        top5.to_csv('Lowmobile.csv')
        print(top5)



s=flipkart()

s.laptop()
s.mobile()













