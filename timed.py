import time
import timeit
import random

level1 = {"potato" : 2, 
          "carrot" : 1, 
          "asparagus" : 5, 
          "broccoli" : 4, 
          "corn" : 3
}
level2 = {"wheat" : 2, 
          "flour" : 1, 
          "bread": 5, 
          "biscuits": 4, 
          "cake": 3}

level3 = {"basil": 3, 
          "cilantro": 2,
          "dill": 5, 
          "parsley": 1, 
          "chives": 4}

level4 = {"strawberry": 3, 
          "apple": 1, 
          "orange": 2, 
          "blueberries": 4,
          "raspberries": 5}

customer_satisfaction = 0

def level_check_method(user_input, crops_for_sale, customer_satisfaction): 
    bank = []
    correct = set(user_input) & set(crops_for_sale)
    for crop in correct:
        bank.append(crops_for_sale[crop])
    bank_balance = sum(bank)
    customer_satisfaction -= len(set(user_input) ^ set(crops_for_sale))* .10
    return (bank_balance, customer_satisfaction)


def timed (user):
    
    #test input for my function
    crops = ["potato", "carrot", "asparagus", "broccoli", "corn" ]
    print("You are asked to type these crops")
    print("Type all the words in time or else you lose.")
    
    initial = time.time()
    
    #list comprehension for plushies
    for crop in crops:
        naming = input("Enter crop {crop}:")
        return 
    
    after = time.time()
    
    duration = (after - initial)
    print(duration)
    
    if duration < 30:
        print("You made it in time! You advance to the next level")
    else:
        print("You did not make it in time :/ you lose a level.")
    
timed("player1")
