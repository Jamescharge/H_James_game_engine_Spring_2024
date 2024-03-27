#my very real atempt of trying to loop things (it was silly)
import time

import pygame as pg

def hasloop():
    looping1 = True
    looping2 = False
    while looping1:
        time.sleep(1)
        print("frame 1")
        time.sleep(2)
        print("frame 2")
        time.sleep(3)
        print("frame 3")
        time.sleep(4)
        print("frame 4")
        time.sleep(5)
        print("frame 5")
        looping1 = False
        looping2 = True
        #could have just "hasloop()" and it would have worked but now I make it more complicated
    while looping2:
        time.sleep(1)
        print("frame 1")
        time.sleep(2)
        print("frame 2")
        time.sleep(3)
        print("frame 3")
        time.sleep(4)
        print("frame 4")
        time.sleep(5)
        print("frame 5")
        hasloop()
hasloop()
import random 
# def anotherloop():
#     framing_again = ['another frame 1','another frame 2','another frame 3','another frame 4','another frame 5',]
#     time.sleep(1)
#     random.choice = framing_again
#     print(str(framing_again))
#     anotherloop()