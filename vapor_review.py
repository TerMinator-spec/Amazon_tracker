# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:57:20 2020

@author: Aman
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)

'''def get_chrome_web_driver():
    return webdriver.Chrome("chromedriver.exe")

driver=webdriver.Chrome("chromedriver.exe", chrome_options=options)
driver=get_chrome_web_driver()'''
url="https://www.trustpilot.com/review/googlemaps.dk"
driver.get(url)

#heading=driver.find_elements_by_xpath('//*[@id="5f932571798e6f0aa0acfea5"]/section/div/div/h2/a')

names=driver.find_elements_by_class_name("consumer-information__name")
headings=driver.find_elements_by_class_name("review-content__title")
reviews=driver.find_elements_by_class_name("review-content__text")

nextpg=driver.find_element_by_xpath('/html/body/main/div/div[4]/section/div[3]/nav/a[7]')
nextpg.send_keys(Keys.ENTER)

Name=[]
Heading=[]
Review=[]
j=0
while(j<2):
    try:
        '''names=driver.find_elements_by_class_name("consumer-information__name")
        headings=driver.find_elements_by_class_name("review-content__title")
        reviews=driver.find_elements_by_class_name("review-content__text")
        for i in range(len(names)):
            Name.append(names[i].text)
        for k in range(len(headings)):
            Heading.append(headings[k].text)
        for j in range(len(reviews)):
            Review.append(reviews[j].text)
        nextpg=driver.find_element_by_xpath('/html/body/main/div/div[4]/section/div[3]/nav/a[7]')
        nextpg.send_keys(Keys.ENTER)  '''
        
        review_list=driver.find_elements_by_class_name("review-card")
        for i in range(len(review_list)):
            nam=review_list[i].find_elements_by_class_name("consumer-information__name")
            if(len(nam)!=0):
                Name.append(nam[0].text)
            else:
                Name.append("")
                
            hd=review_list[i].find_elements_by_class_name("review-content__title")
            if(len(hd)!=0):
                Heading.append(hd[0].text)
            else:
                Heading.append("")
                
            rv=review_list[i].find_elements_by_class_name("review-content__text")
            if(len(rv)!=0):
                Review.append(rv[0].text)
            else:
                Review.append("")
        nextpg=driver.find_element_by_xpath('/html/body/main/div/div[4]/section/div[3]/nav/a[3]')
        nextpg.send_keys(Keys.ENTER)    
        j=j+1
            
    except Exception as e:
        print(e)

dicts={"names":Name[:38], "Headings": Heading[:38], "Reviews":Review[:38]}       
import pandas as pd 
df=pd.DataFrame(dicts)
df.to_csv("googlemap_review.csv")
        
#revw=driver.find_elements_by_xpath('//*[@id="5f8e4407798e6f0aa0a95a48"]/section/div/div[2]/p')
lits=driver.find_elements_by_class_name("review-card")
nem=lits[0].find_elements_by_class_name("consumer-information__name")
rv=lits[4].find_elements_by_class_name("review-content__text")

//*[@id="5f932571798e6f0aa0acfea5"]











