import pyautogui as pag
import random
import time
import keyboard

if keyboard.is_pressed('q'):
    print("Hello!")

notpressed = True
while True:
        x = random.randint(900,1500) #setting X axis
        y = random.randint(400,800) #setting Y axis
        pag.moveTo(x,y,0.2) #move to X and Y on an interval in seconds
        time.sleep(1)
           
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('Ending')
                break  # finishing the loop 