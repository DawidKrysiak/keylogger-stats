import os
import pynput
import collections
from collections import Counter
from pynput.keyboard import Key, Listener

keys_pressed =[]
report = []
def on_press(key):
    keys_pressed.append(key)

def on_release(key):
    if key == Key.esc:
        for value,count in collections.Counter(keys_pressed).most_common():
            if count >1:
                line = ('%s,%1d' %(value,count))
                list = line.split(",")
                report.append(list)   
        while report:
            print(report.pop(0))
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
