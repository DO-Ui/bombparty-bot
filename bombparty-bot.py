import pynput
from pynput import keyboard
import os
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
# import PIL
# from PIL import ImageGrab
import io
# from PIL import Image
import random
import pyperclip

send = KeyboardController()
mouse = MouseController()

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

with open(CURR_DIR + r"\wordlist.txt",
          encoding="utf8") as f:
    content = f.readlines()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

usedletters = []
atoz = []

def on_activate():
    pos = mouse.position
    mouse.position = (810, 555)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    send.press(Key.ctrl)
    send.press('c')
    time.sleep(0.01)
    send.release('c')
    send.release(Key.ctrl)
    
    time.sleep(0.1)

    result = pyperclip.paste()
    time.sleep(0.01)
    pyperclip.copy('')

    mouse.position = (pos)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    
    search = result.lower()
    search = search.strip()
    # print(search)
    found = []
    for i in content:
        if (i.find(search) != -1):
            found.append(i)
    
    arrsize = len(found)
    if (arrsize == 0):
        return print("error")

    choice = random.randint(0, arrsize-1)
    
    for char in found[choice]:
        usedletters.append(char)
        send.press(char)
        send.release(char)
        time.sleep(0.096)
    nodups = list(dict.fromkeys(usedletters))
    atoz = sorted(nodups)
    time.sleep(0.02)
    send.press(Key.enter)
    send.release(Key.enter)
            
def reset_bonus():
    usedletters = []
    nodups = []
    atoz = []

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<f8>'),
    on_activate)

with keyboard.Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)) as l:
    l.join()



