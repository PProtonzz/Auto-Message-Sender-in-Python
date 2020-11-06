"""
***Sending Automated messages or Comments**** 

Warning: DO NOT USE THIS FOR VIOLATION

""""""
by: Pranav Fulkari
mail: director@bottlecaptech.com
blog: https://pranavfulkari.com/

python version: python3.7.1
"""

import pyautogui
from time import sleep
from random import randint

x = 50   #how many messages or comments you want to send

def name():
    """generates random names"""

    nameList = ["Baby", "Shona", "Honey", "Jaan", "Wifey"]   #list of names (change according to your requirement)
    rand_name = nameList[randint(0, len(nameList) - 1)]      #traverse names randomly for n, from 0 to (n-1)

    return rand_name    #return the random name it just generated
 


while True:      #forever loop
    pyautogui.typewrite(f"I love you {name()}")  #type message
    sleep(.600)                        #A bit delay of 600 ms
    pyautogui.typewrite("\n")          #New line, here 'Enter' to send text
    sleep(2)                           #delay of 2 seconds

    x = x - 1         #decrement x value by 1

    if x == 0:       
        break         #get out of the loop and finish
