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

level1 = {"potato" : 2, 
          "carrot" : 1, 
          "asparagus" : 5, 
          "broccoli" : 4, 
          "corn" : 3
}
level2 = ["wheat", "flour", "bread", "biscuits"]
level3 = ["basil", "cilantro" "dill", "parsley"]
level4 = ["strawberry", "apple", "orange", "blueberries"]

customer_satisfaction = 1

def level_check_method(user_input, crops_for_sale, customer_satisfaction): 
    bank = []
    correct = set(user_input) & set(crops_for_sale)
    for crop in correct:
        bank.append(crops_for_sale[crop])
    bank_balance = sum(bank)
    customer_satisfaction -= len(set(user_input) ^ set(crops_for_sale))* .10
    return (bank_balance, customer_satisfaction)
