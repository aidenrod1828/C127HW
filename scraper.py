from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    star_table=soup.fine("table")
    temp_list=[]
    table_rows=star_table.find_all("tr")
    for tr in table_rows:
        td=tr.fine_all("td")
        row=[i.text.rstrip() for i in td]
        temp_list.append(row)
        
with open("scrapper_2.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
scrape()