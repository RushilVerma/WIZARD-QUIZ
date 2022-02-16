#Code for WebScrapping 
#Author: Rushil Verma
#Description : For Answering Wizard 101 Trivia Quiz
#remove below comments to use 


from __future__ import unicode_literals
from bs4 import BeautifulSoup
from matplotlib.style import use
import pandas as pd
from selenium import webdriver
import webbrowser
import time

#importing user defined function
from solveit import solve
from alreadyloggedin import nextquiz

url = "https://www.wizard101.com/game"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
username = 'rushilverma101'
passcode = 'wiHappy@jat07'
driver = webdriver.Chrome('D:\Project\PythonWebScraping\chromedriver_win32\chromedriver.exe')
driver.get(url)
time.sleep(1)
#90003166
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/dl/dd/ul/li/div/form/div[2]/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/dl/dd/ul/li/div/form/div[3]/input").send_keys(passcode)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/dl/dd/ul/li/div/form/table/tbody/tr/td[1]/div/div/input").click()
time.sleep(1)

print("press ENTER key after solving captcha and logging in:")
input()

nextquiz(driver)
#keep at the end of the code 
driver.quit()