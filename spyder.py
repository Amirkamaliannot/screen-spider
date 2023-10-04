# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:15:10 2022

@author: Amir
"""

import pyautogui
import time
from PIL import Image

page_number = 581
time.sleep(5)

page_list = []

# cover = pyautogui.screenshot(region=(417, 120, 570 , 900  ))
# cover = cover.rotate(90, expand=1)
# pyautogui.click(1005, 175)
# pyautogui.click(1005, 175)
# time.sleep(5)
print(1)
for i in range(page_number):
    
    # time.sleep(0.25)
    img = pyautogui.screenshot(region=(417, 55, 570 , 963 ))
    # img = img.rotate(90, expand=1)
    page_list.append(img)
    # pyautogui.click(450, 120)
    # pyautogui.moveTo(450, 520)
    # pyautogui.mouseDown(button='left')
    # pyautogui.moveTo(550, 520, 0.1)
    
    pyautogui.click(1005, 175)
    pyautogui.moveTo(1200, 700)

    # pyautogui.dragTo(850, 1040, button='left', duration=0.2)

    time.sleep(0.25)
    img.save(r'.\file name.jpg')

img.save(r'.\file name.pdf')

cover.save("out.pdf", save_all=True, append_images=page_list)

