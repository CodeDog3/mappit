import sys
import webbrowser
import pyperclip
import os
from datetime import date
import subprocess as sp
import re

###################################################################################
def Help():
    os.chdir('c:\\Users\\jonbr\\mappit\\mappit')
    sp.Popen(['notepad.exe', 'help.txt'])
    return True

def History():
    os.chdir('c:\\Users\\jonbr\\mappit\\mappit')
    sp.Popen(['notepad.exe', 'history.txt'])
    return True

def write_history(address):
    os.chdir('c:\\Users\\jonbr\\mappit\mappit')
    history = open('history.txt', 'a')
    today = date.today()
    day = today.strftime('%b-%d-%Y')

    history.write('==========================\n')
    history.write(day + ': ' + address+'\n')
    history.close()
####################################################################################

#used to stop web execution if flag is used
blocking = False
#greedy matching to find if any flags occur
flagCheck = re.compile(r'-+(h|d|w).*')
mo = flagCheck.search(' '.join(sys.argv[1:]))

try:
    if (mo.group() == '-help' or mo.group() == '-h'):
        print('works for help')
        #returns true and blocks
        blocking = Help()
    elif (mo.group() == '-drive' or mo.group() == '-d'):
        print("works for drive")
        blocking = True
    elif (mo.group() == '-walk' or mo.group() == '-w'):
        print("works for walk")
        blocking = True
    elif (mo.group() == '-history' or mo.group() == '--h'):
        print('works for history')
        #returns true and blocks
        blocking = History()
        
except:
    print("initiating lookup")

if(blocking == False):
    if (len(sys.argv)) > 1:
        arguments = sys.argv[1:]
        address = ' '.join(arguments)
    else:
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)
    #keeps a history of searches in history.txt
    write_history(address)


