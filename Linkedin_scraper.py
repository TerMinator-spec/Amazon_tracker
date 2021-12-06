# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:35:34 2020

@author: Aman
"""


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import Select
def get_chrome_web_driver():
    return webdriver.Chrome("chromedriver.exe")

driver=get_chrome_web_driver()

link=driver.find_element_by_xpath('//*[@id="inducteesEE"]/li[10]/a')
site=link.get_attribute("href")
driver.get('https://www.linkedin.com/in/greggmortonjr/')

nme=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/ul[1]/li[1]')
comp=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/h2')
livin=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/ul[2]/li[1]')


sind=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/ul[2]/li[3]/a')
driver.get(sind.get_attribute("href"))

info=driver.find_elements_by_class_name('pv-contact-info__ci-container')

cntct=driver.find_element_by_xpath('//*[@id="ember334"]/div/section[1]/div/a')
twit=driver.find_element_by_xpath('//*[@id="ember334"]/div/section[2]/ul/li/a')

//*[@id="ember147"]/div/section[1]/div/a
//*[@id="ember147"]/div/section[1]/div

list2=driver.find_elements_by_xpath('//*[@id="inducteesEE"]/li/a')
links=[]
for i in range(len(list2)):
    try:
        
        links.append(list2[i].get_attribute('href'))
        
    except Exception as e:
                print("Didn't get any products...")
                print(e)

name=[]
company=[]
location=[]  
contacts=[]              
for i in range(len(links)):
    
    try:
        driver.get(links[i])
        nme=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/ul[1]/li[1]').text
        comp=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/h2').text
        livin=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/ul[2]/li[1]').text
        
        name.append(nme)
        company.append(comp)
        location.append(livin)
        
        sind=driver.find_element_by_xpath('//*[@id="ember60"]/div[2]/div[2]/div[1]/ul[2]/li[3]/a')
        driver.get(sind.get_attribute("href"))
        
        info=driver.find_elements_by_class_name('pv-contact-info__ci-container')
        
        for j in range(len(info)):
            contacts.append(info[j].text+", ")
            
    except Exception as e:
        print("sorry")
    
    


    
    

