from numpy import ModuleDeprecationWarning
import pyautogui,time
 
print("Starting in 5 sec .....")
time.sleep(5)
ty="Anime Dekhna Shuru kar ab"
  
for i in range (10):
    pyautogui.typewrite(ty)
    pyautogui.press("Enter")
