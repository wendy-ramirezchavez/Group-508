import time
import timeit
import random

def timed (user):
    
    #test input for my function
    plushies = ["kitty", "bear", "flower", "bunny"]
    print("You are asked to type these plushies")
    print("Type all the words in time or else you lose.")
    
    initial = time.time()
    
    #list comprehension for plushies
    for plush in plushies:
        naming = input("Enter plushie {plush}")
        return 
    
    after = time.time()
    
    duration = (after - initial)
    print(duration)
    
    if duration < 30:
        print("You made it in time! You advance to the next level")
    else:
        print("You did not make it in time :/ you lose a level.")
    
timed("player1")