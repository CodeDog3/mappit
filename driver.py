import sys
import webbrowser
import pyperclip
import os

#path = os.path.abspath("src/driver.py")

if (len(sys.argv)) > 1:
    arguments = sys.argv[1:]
    address = ' '.join(arguments)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' +address)