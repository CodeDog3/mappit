import sys
import webbrowser
import pyperclip
import os
from datetime import date
import subprocess
import re


def Help():
    os.chdir('c:\\Users\\jonbr\\mappit\\mappit')
    if (os.path.exists(os.getcwd+'\\help.txt')):
        os.system('help.txt')

def History():
    os.chdir('c:\\Users\\jonbr\\mappit\\mappit')
    if (os.path.exists(os.getcwd+'\\history.txt')):
        os.system('history.txt')

def write_history(address):
    os.chdir('c:\\Users\\jonbr\\mappit\mappit')
    history = open('history.txt', 'a')
    today = date.today()
    day = today.strftime('%b-%d-%Y')

    history.write('==========================\n')
    history.write(day + ': ' + address+'\n')
    history.close()

arguments = sys.argv[1:]
# test = ','.join(arguments)
# tester = re.compile(r'(*,){1}')
# tt = tester.search(test)

try:
    if (sys.argv == 'help' or 'h'):
        Help()
    elif (sys.argv[1].lower() == 'drive' or 'd'):
        print("a")
    elif (sys.argv[1].lower() == 'walk' or 'w'):
        print("b")
    elif (sys.argv[1] == ('history' or '-h')):
        #webbrowser.open('https://www.google.com/maps/place/')
        History()
except:
    if (len(sys.argv)) > 1:
        address = ' '.join(arguments)
    else:
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' +address)
    #keeps a history of searches in history.txt
    write_history(address)


