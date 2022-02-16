from __future__ import unicode_literals
from bs4 import BeautifulSoup
from matplotlib.style import use
import pandas as pd
from selenium import webdriver
import webbrowser
import time

#importing user defined function
from solveit import solve

def nextquiz(driver):
    
    usertext = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/dl/dt[2]/a/div").text
    print("Username: (",usertext,")")

    print("-------login page done----")

    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/dl/dd/ul/li/div/a[5]").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div/div[2]/div/a").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td/div/table[2]/tbody/tr[2]/td[2]/p/b/a").click()

    print("press ENTER key after selecting a QUIZ :")
    input()

    #to read to detect quiz name and question
    quizname = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div/div[1]/h1").text

    print("the quiz is : ", quizname )
    #loading respective file
    import json
    filename = quizname+".json"
    # Opening JSON file
    try:

        with open(filename, 'r',encoding="utf8") as openfile:
        
            # Reading from json file
            json_object = json.load(openfile)

    except:
        print("You entered this quiz: ",filename[:-5])
        print("Please enter correct quizs from these:")
        print("Pirate101 Adventure Trivia")
        print("Pirate101 Fun Trivia")
        print("Pirate101 Skyways Trivia")
        print("Wizard101 Conjuring Trivia")
        print("Wizard101 Magical Trivia")
        print("Wizard101 Marleybone Trivia")
        print("Wizard101 Mystical Trivia")
        print("Wizard101 Spellbinding Trivia")
        print("Wizard101 Spells Trivia")
        print("Wizard101 Wizard City Trivia")
        print("Wizard101 Zafaria Trivia")
        nextquiz(driver)
        return

    #load json quiz file 
    #total 12 questions
    #at last question we dont need to click next question
    for a in range(11):
        solve(driver,json_object)

        #clicking next question button
        
        driver.find_element(webdriver.common.by.By.ID,"nextQuestion").click()

        time.sleep(3)

    solve(driver,json_object)
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[2]/div[3]/button").click()
    time.sleep(1)

    #claim your reward
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[3]/div[3]/a").click()
    time.sleep(1)

    import json    
    with open(filename, "w",encoding="utf8") as outfile:
        json.dump(json_object, outfile)
        
    print("New answers saved !!")
    print("Press Enter key after solving the catpcha and claiming reward  :")
    print(" for the next quiz")
    print("Input 'q' if you want to exit")
    inp = input()
    if(inp == "q"):
        driver.quit()
    else:
        nextquiz(driver)





