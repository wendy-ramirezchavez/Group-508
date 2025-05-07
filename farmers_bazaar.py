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
class FarmersBazaar():


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
    print(f"You are asked to type these crops:{crops}")
    print("when you are finished, type 'done' ")
    print("Type all the words in time or else you lose.")
    
    initial = time.time()
    answers = []
         
    while True:
        naming = input("Enter crop: ")
        if naming == "done":  
            break
        answers.append(naming)
    
    after = time.time()
    
    duration = (after - initial)
    print(duration)
    
    if duration < 30:
        print("You made it in time! You advance to the next level")
    else:
        print("You did not make it in time :/ you lose a level.")
    return answers , duration < 30


    
answer, duration = timed("player1") 


def new_level_crops(crop_list, available_crops, bank_balance, crops_sold, 
                    crop_thresholds, unlocked_levels):

    bank_limit = {
    1: 15,
    2: 30,
    3: 45,
    4: 60
    
}
    if bank_balance >= bank_limit and crops_sold >= crop_limit:
        if i < len(available_crops) and available_crop[i] not in crop_list:
            crop_list.append(available_crops[i])
            print (f"Yayyyyy! You've unlocked a new crop: {available_crops[i]}")
            
            
    for level, threshold in bank_limit.items():
        if bank_balance >= threshold and level not in unlocked_level:
            unlocked_levels.add(level)
            print(f"Yayyyy! Level {level} unlocked!")
        
        
        return crop_list, unlocked_levels
def upgrade(player_level,completed_tasks, daily_tasks, max_level=10):
    need_tasks = daily_tasks.get(player_level,[])

    for task in need_tasks:
        if task not in completed_tasks:
            return player_level, [], {"finish all the task to level up"}
    
    player_level +=1
    tasks_unlock = daily_tasks.get(player_level,[])
    
    rewards = {}
    if 1<= player_level <= 4:
        rewards["starter_kit"] = True
    elif 5 <= player_level <= 9:
        rewards["upgrade_crops"] = True
    else: 
        rewards["premium_market"] = True
        
    return player_level, tasks_unlock, rewards
        
        # Some daily tasks for each level
daily_task = {
    1: ["watering", "fertilizing"],
    2: ["protecting", "harvesting"],
    3: ["watering", "harvesting", "fertilizing"]
}

if __name__ == "__main__":
    player_level = 1
    completed_tasks = ["watering", "fertilizing"]
    new_level, tasks_unlock, rewards = upgrade(player_level,completed_tasks, daily_task)
    
    print("New Level:", new_level)
    print("Unlock Tasks:", tasks_unlock)
    print("Rewards:", rewards)
