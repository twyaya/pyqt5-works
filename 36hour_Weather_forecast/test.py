# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:04:17 2019

@author: user
"""

import pyautogui, time


time.sleep(2)

pyautogui.moveTo(876 ,628)
pyautogui.click()
time.sleep(1)

try:
    for i in range(21):
        pyautogui.moveTo(886, 385)  #選像欄
        pyautogui.click()
        pyautogui.keyDown('down')
        time.sleep(1)


        pyautogui.moveTo(876 ,628)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo(1004, 624)
        pyautogui.click()
        
        
        
except KeyboardInterrupt:               # 處理 Ctrl-C 按鍵
  print('\nDone.')
  
