# área de trabalho > google chrome > digita hbo > clica no perfil > digita big bang theory > play

import pyautogui
import time

pyautogui.alert("Clique OK para começar")
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('hbomax')
pyautogui.press('enter')
time.sleep(5)
pyautogui.position(187, 567)
pyautogui.click()
time.sleep(3)
pyautogui.position(187, 567)
pyautogui.moveTo(150,95)
pyautogui.click()
pyautogui.write('the big bang theory')
time.sleep(3)
pyautogui.moveTo(300,300)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(200,700)
pyautogui.click()
time.sleep(5)
pyautogui.press('f11')

