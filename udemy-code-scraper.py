import requests
from bs4 import BeautifulSoup as bs
import csv

coupons = []

def scrapeSite(url, pageNo):
    # print(f"Attempting scrape page number {pageNo} \n")
    page = requests.get(url + pageNo)
    if page.status_code == 200:
        soup = bs(page.content, 'html.parser')
        links = soup.find_all('a', class_='card-header')
        if(links):
            for link in links:
                url = link['href'].replace("English", "go")
                # print(url)
                couponPage = requests.get(url)
                if couponPage.status_code == 200:
                    coupSoup = bs(couponPage.content, 'html.parser')
                    coupon = coupSoup.find(id="couponLink")
                    coupons.append([coupon['href']])


siteUrl = "https://www.discudemy.com/language/English/"
    
noPages = 5

if(noPages):
    for i in range(1,noPages+1):
        scrapeSite(siteUrl, str(i))
    f = open("links.csv", "w")
    writer = csv.writer(f)
    print(coupons)
    writer.writerows(coupons)
else:
    print("Attempting scrape all \n")
    scrapeSite(siteUrl, "0")
