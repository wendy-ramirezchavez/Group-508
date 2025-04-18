import time
import timeit
import random

def timed ():
    
    initial = time.sleep(random.random(0,6)) 
    actual = time.time()
    
    harvest = (actual - initial)
    
    if harvest < initial:
        print("You advance to the next level")
    else:
        print ("You lose one level")
     
