"""
Robotic comment code using python pyAutogui

A code that automatically types comments and presses 'Enter' to send 
the comment.
It sends 5000 comments after 2 seconds delay.
"""
"""
by: Pranav Fulkari
mail: director@bottlecaptech.com
blog: https://pranavfulkari.com/
"""

"""
You must have pyautogui installed in your pc.
If not try 'pip install pyautogui'  command.
"""


from time import sleep  #import sleep for delay
import pyautogui      #import pyautui package to use the keyboad in our case
x = 5000              #How many messages do I want to send

while True:     #forever loop
    pyautogui.typewrite("I Love You.")  #type in the messsage
    sleep(.600)   #a bit delay of 600 ms
    pyautogui.typewrite("\n")  #Hit 'Enter' 
    sleep(2)                #delay of 2 seconds
    x = x - 1     #decrement x
    if x == 0:   #if x = 0 break the loop stop the code
        break     #break the loop

"""
"""
