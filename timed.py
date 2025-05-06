import time
import timeit
import random

def timed (user):
    
    #test input for my function
    crops = ["radish", "rutabaga", "tomato", "pumpkin"]
    print(f"You are asked to type these plushies: {crops}")
    print("Type all the words in time or else you lose.")
    
    initial = time.time()
    
    #list comprehension for plushies
    for crop in crops:
        naming = input(f"Enter plushie: {crop}")
    
    after = time.time()
    
    duration = (after - initial)
    print(duration)
    
    if duration < 30:
        print("You made it in time! You advance to the next level")
    else:
        print("You did not make it in time :/ you lose a level.")
    
timed("player1")