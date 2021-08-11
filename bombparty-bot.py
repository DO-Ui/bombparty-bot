import pynput
from pynput import keyboard
import os
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import io
import random
import pyperclip

send = KeyboardController()
mouse = MouseController()

SET_THIS_TO_True_FOR_LONG_WORDS = False

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

with open(CURR_DIR + r"\wordlist.txt",
          encoding="utf8") as f:
    content = f.readlines()


def on_activate():
    pos = mouse.position
    mouse.position = (835, 575)
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
    # mouse.press(Button.left)
    # mouse.release(Button.left)

    search = result.lower()
    search = search.strip()
    found = []
    for i in content:
        if (i.find(search) != -1):
            found.append(i)

    arrsize = len(found)
    if (arrsize == 0):
        return print("error")

    l = 0

    if (SET_THIS_TO_True_FOR_LONG_WORDS):
        for i in range(len(found)):
            if len(found[i]) > l:
                l = i
        choice = l
    else:
        choice = random.randint(0, arrsize - 1)

    for char in found[choice].strip():
        send.press(char)
        send.release(char)
        time.sleep(0)
    time.sleep(0.00001)
    send.press(Key.enter)
    send.release(Key.enter)
    print(found[choice])


def reset_bonus():
    usedletters = []
    nodups = []
    atoz = []


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = keyboard.HotKey(keyboard.HotKey.parse('<f8>'), on_activate)

with keyboard.Listener(on_press=for_canonical(hotkey.press),
                       on_release=for_canonical(hotkey.release)) as l:
    l.join()
