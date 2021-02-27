import pynput
from pynput import keyboard
import os
import time
from pynput.keyboard import HotKey, Key, Controller, Listener
import PIL
from PIL import ImageGrab
import io
from PIL import Image
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

filepath = r'C:\Users\zZDOU\Downloads\bombparty ruiner\capture.png'

send = Controller()

with open(r"C:\Users\zZDOU\Downloads\bombparty ruiner\wordlist.txt", encoding="utf8") as f:
    content = f.readlines()

def on_activate():
    screenshot = ImageGrab.grab(bbox=(780, 540, 840, 570))
    screenshot.save(filepath, 'PNG')
    try:
        result = pytesseract.image_to_string(Image.open(r"C:\Users\zZDOU\Downloads\bombparty ruiner\capture.png"), timeout=3)
    except RuntimeError as timeout_error:
        print("timeout")
        pass
    
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

    rand = random.randint(0, arrsize-1)
    for char in found[rand]:
        send.press(char)
        send.release(char)
        time.sleep(0.0001)
    time.sleep(0.04)
    send.press(Key.enter)
    time.sleep(0.001)
    send.release(Key.enter)
            

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<f8>'),
    on_activate)

with keyboard.Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)) as l:
    l.join()



