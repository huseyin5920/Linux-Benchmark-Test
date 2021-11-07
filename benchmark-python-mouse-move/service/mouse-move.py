import pyautogui


# EKRAN ÇÖZÜNÜRLÜK BİLGİSİ
pyautogui.size()
print(pyautogui.size())

# deneme1 tıkla
pyautogui.moveTo(60, 300, duration=1)
pyautogui.doubleClick()

pyautogui.click(1900, 50, duration=1)
pyautogui.click("deneme2")
# # deneme2 tıkla
# pyautogui.moveTo(60, 400, duration=1)
# pyautogui.doubleClick()
# pyautogui.click(1900, 50, duration=1)


# # deneme3 tıkla
# pyautogui.moveTo(60, 500, duration=1)
# pyautogui.doubleClick()
# pyautogui.click(1900, 50, duration=1)

# print(pyautogui.getWindowsWithTitle())
#pyautogui.moveRel(-400, 0, duration=0.5)
