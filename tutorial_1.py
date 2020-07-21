# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:11:48 2020

@author: OHyic
"""


#import selenium drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 

#get selenium webdriver path
webdriver_path = "C:\\Users\\OHyic\\Desktop\\selenium_python_tutorials\\chromedriver.exe"

#create a driver
driver = webdriver.Chrome(webdriver_path)

driver.get("https://www.google.com")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("Hello World")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)