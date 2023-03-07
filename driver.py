#Name: Jon Brennan
#Description: script to quickly search for directions with a simple run command from terminal/windows run
#Purpose: practice web scraping/file directories/regex/selenium/batch and test limitations also to practice writing clean legible code readable to others

##################################################################################
#Imports
import sys #used to read arguments in run
import webbrowser #used to open google maps
import pyperclip #used to read clipboard
import os #used for file navigation
from datetime import date #used to write the date in time to history
import subprocess as sp #used to open notepad documents upon request
import re #used for regex to determine if a command is called
from selenium import webdriver #used to access webbrowser and functions
from selenium.webdriver.common.by import By #used to search for web selectors
from selenium.webdriver.support.wait import WebDriverWait #used to wait for program to respond before searching (async/await)
from selenium.webdriver.support import expected_conditions as EC #used for expected conditions function - presence of element
import time #stalls between clicks to give time for page to load

###################################################################################
#opens a notepad showing useful commands
def Help():
    cwd = os.getcwd()
    os.chdir(cwd+'\\mappit\\mappit')
    sp.Popen(['notepad.exe', 'help.txt'])
    return True

#opens up prior search history
def History():
    cwd = os.getcwd()
    os.chdir(cwd+'\\mappit\\mappit')
    sp.Popen(['notepad.exe', 'history.txt'])
    return True

#writes to history notepad
def write_history(address):
    cwd = os.getcwd()
    os.chdir(cwd+'\\mappit\\mappit')
    history = open('history.txt', 'a')
    today = date.today()
    day = today.strftime('%b-%d-%Y')

    history.write('==========================\n')
    history.write(day + ': ' + address+'\n')
    history.close()
####################################################################################
#used to stop web execution if flag is called
blocking = False
#used to see if we need selenium, different mode of execution
selenium = False
walk = False
drive = False
#greedy matching to find if any flags occur
flagCheck = re.compile(r'-+(h|d|w)([\S].[\S])*')
mo = flagCheck.search(' '.join(sys.argv[1:]))

try:
    if (mo.group() == '-help' or mo.group() == '-h'):
        print('works for help')
        #returns true and blocks
        blocking = Help()
    elif (mo.group() == '-drive' or mo.group() == '-d'):
        print("works for drive")
        selenium = True
    elif (mo.group() == '-walk' or mo.group() == '-w'):
        print("works for walk")
        selenium = True
        walk = True
    elif (mo.group() == '-history' or mo.group() == '--h'):
        print('works for history')
        #returns true and blocks
        blocking = History()
    
    arguments = sys.argv[1:]
    #removes flags for searching
    arguments = ' '.join(arguments).replace(mo.group(), '')
        
except:
    print("initiating lookup")

if(blocking == False and not selenium):
    if (len(sys.argv)) > 1:
        arguments = sys.argv[1:]
        address = ' '.join(arguments)
    else:
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)
    #keeps a history of searches in history.txt
    write_history(address)

#uses selenium to navigate according to flags for user
#firefox is more friendly and works better with selenium, chrome needs api
elif(blocking == False and selenium):
    if (len(sys.argv)) > 1:
        address = arguments
    else:
        address = pyperclip.paste()

    browser = webdriver.Firefox()
    browser.get('https://www.google.com/maps/place/' + address)
    #clicks search button so address stays when clicking "directions"
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'searchbox-searchbutton')))
    elem.click()
    time.sleep(2)
    #clicks direction button
    elem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.Pf6ghf.ecceSd.tLjsW > div.etWJQ.jym1ob.kdfrQc.pChizd.bWQG4d > button' )))
    elem.click()
    time.sleep(2)

    #if walk flag set will also click walk button
    if(walk == True):
        elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR ,'div.oya4hc:nth-child(4) > button:nth-child(1)')))
        elem.click()
    else:
        elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR ,'div.oya4hc:nth-child(2) > button:nth-child(1)')))
        elem.click()

    #keeps a history of searches in history.txt
    write_history(address)


