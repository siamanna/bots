import pyautogui, time
time.sleep(5)
OurText = open("text.txt", "r")
for text in OurText:
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    