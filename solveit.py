from __future__ import unicode_literals
from bs4 import BeautifulSoup
from matplotlib.style import use
import pandas as pd
from selenium import webdriver
import webbrowser
import time

def solve(driver,json_object):
    try:
        question = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[1]").text
    
    except:
        question = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[1]").text
                                            
    print("Question is :", question,"--")
    
    while question[0:1] == " ":
        question = question[1:]

    answer = ""
    try:
        answer = json_object[question]
    
    except:
        print("Unknown question !!")
        print("Answer is:")
        answer = input();
        json_object.update({question:answer})
    
    finally:
        print("Answer :",answer)
    
    time.sleep(1)
    #/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div[1]/span[2] - text optin 1
    #/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div[2]/span[2] - text optin 2
    #/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div[2]/span[1]/a - button opt 2
    for i in range(4):
        try:

            xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[2]"
            option = driver.find_element_by_xpath(xpath).text
            print("try in option")
        except:
                    #/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[2]/div[4]
            xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[2]"   
            option = driver.find_element_by_xpath(xpath).text
            print("except in option")
        
        if answer == option:
            print("option:",str(i+1),"was",option)
            try:
                xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[1]/a"
                option = driver.find_element_by_xpath(xpath).click()
                print("click1")
            except:
                xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[1]/a"
                option = driver.find_element_by_xpath(xpath).click()
                print("click2")
                
            break
        if i == 3:
            print("Unknown options !!")
            print("Answer is:")
            answer = input();
            json_object.update({question:answer})
            for i in range(4):
                try:

                    xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[2]"
                    option = driver.find_element_by_xpath(xpath).text
                    print("try in option")
                except:
                            #/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[2]/div[4]
                    xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[2]"   
                    option = driver.find_element_by_xpath(xpath).text
                    print("except in option")
                
                if answer == option:
                    print("option:",str(i+1),"was",option)
                    try:
                        xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[4]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[1]/a"
                        option = driver.find_element_by_xpath(xpath).click()
                        print("click1")
                    except:
                        xpath = "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i+1)+"]/span[1]/a"
                        option = driver.find_element_by_xpath(xpath).click()
                        print("click2")
                        
                    break
