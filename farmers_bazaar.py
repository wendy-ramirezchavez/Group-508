import time
import timeit
import random

class FarmersBazaar():

    level1 = {"potato" : 2, 
          "carrot" : 1, 
          "asparagus" : 5, 
          "broccoli" : 4, 
          "corn" : 3}
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
    daily_task = {
        1: ["watering", "fertilizing"],
        2: ["protecting", "harvesting"],
        3: ["watering", "harvesting", "fertilizing"]
    }
   
    def __init__(self):
        self.customer_satisfaction = 1.0
        self.bank_balance = 0
        self.unlocked_levels = {1}
        self.crop_list = list(FarmersBazaar.level1.keys())  
    
    
    def level_check_method(self, user_input, crops_for_sale, customer_satisfaction): 
        bank = []
        correct = set(user_input) & set(crops_for_sale)
        for crop in correct:
            bank.append(crops_for_sale[crop])
            self.bank_balance = sum(bank)
        self.customer_satisfaction -= len(set(user_input) ^ set(crops_for_sale))* .10
        return (self.bank_balance, self.customer_satisfaction)


    def timed (self, crops):
    
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
            print("You made it in time! You advance to the next level. Type (next level) to continue")
        else:
            print("You did not make it in time :/ you lose a level.")
        return answers , duration < 30



    def new_level_crops(self):

        level_next_game = {
         "Level 2": FarmersBazaar.level2,
         "Level 3": FarmersBazaar.level3,
         "Level 4": FarmersBazaar.level4
         }

        bank_limit = {
            1: 15,
            2: 30,
            3: 45,
            4: 60}
            
        for level, threshold in bank_limit.items():
            if self.bank_balance >= threshold and level not in self.unlocked_level:
                self.unlocked_levels.add(level)
                print(f"Yayyyy! Level {level} unlocked!")
        
                new_crops = list(level_daye[level].keys())
                for crop in new_crops:
                    if crop not in self.crop_list:
                        self.crop_list.append(crop)
                print (f"Yayyyy! New crops: {new_crops} unlocked!"")
        
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


def main():
    player_level = 1
    completed_tasks = ["watering", "fertilizing"]
    game = FarmersBazaar()
  
   levels_in_game = {
       "Level 1": FarmersBazaar.level1,
       "Level 2": FarmersBazaar.level2,
       "Level 3": FarmersBazaar.level3,
       "Level 4": FarmersBazaar.level4
       }
    
    for level in range(1, 4):
        if level not in game.unlocked_levels:
            continue
  
   print(f"Total Bank Balance: ${game.bank_balance}")
   print(f"Total Customer Satisfaction: {game.customer_satisfaction}")
      
    
if __name__ == "__main__":
    player_level = 1
    completed_tasks = ["watering", "fertilizing"]
    new_level, tasks_unlock, rewards = upgrade(player_level,completed_tasks, daily_task)
    
    print (f"")
    print("New Level:", new_level)
    print("Unlock Tasks:", tasks_unlock)
    print("Rewards:", rewards)

