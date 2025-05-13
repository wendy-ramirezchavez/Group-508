import time
import timeit
import random

class FarmersBazaar():
    level1 = {"potato" : 2,"carrot" : 1, "asparagus" : 5, "broccoli" : 4, "corn" : 3}
    level2 = {"wheat" : 2, "flour" : 1, "bread": 5, "biscuits": 4,  "cake": 3}
    level3 = {"basil": 3, "cilantro": 2, "dill": 5,"parsley": 1, "chives": 4}
    level4 = {"strawberry": 3,  "apple": 1,"orange": 2,  "blueberries": 4,"raspberries": 5}
    
    daily_task = {
        1: ["watering", "fertilizing"],
        2: ["planting", "harvesting"],
        3: ["baking", "packaging"],
        4: ["marketing", "distributing"]
    }
    
    def __init__(self):
        self.customer_satisfaction = 1.0
        self.bank_balance = 0
        self.crop_list = list(FarmersBazaar.level1.keys())
        self.unlocked_levels = {1}
        self.player_level = 1
        self.completed_tasks = ["watering", "fertilizing"]
        self.current_order = None


    def level_check_method(self,user_input, crops_for_sale): 
        bank = []
        correct = set(user_input) & set(crops_for_sale)
        for crop in correct:
            bank.append(crops_for_sale[crop])
        self.bank_balance += sum(bank)
        self.customer_satisfaction -= len(set(user_input) ^ set(crops_for_sale))* .10
        return sum(bank), self.customer_satisfaction


    def timed (self, crops):
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
    
        duration = after - initial
        print(duration)
    
        if duration < 30 and self.customer_satisfaction == 100:
            print("You made it in time! You advance to the next level. Type (next level) to continue")
            return answers, True
        if duration < 30 and self.customer_satisfaction != 100:
            print("""
                  \nYou forgot a crop to bring to the farmers market your customers were not happy... 
                  \nkeep an eye on your decreasing customer satisfaction. """)
            self.customer_satisfaction -= 0.2
            return answers, False
        else:
            print("You did not make it in time, your customers were not happy.")
            self.customer_satisfaction -= 0.2
            return answers, False
        
    def new_order(self, crop_order):
        crop = random.choice(list(crop_order.keys()))
        quantity = random.randint(2, 4)
        total = quantity * (crop_order[crop]+1)
        self.current_order = {
            "crop": crop,
            "quantity": quantity,
            "total": total
        }
        print(f"Please fulfill! {quantity} {crop}. Total: ${total}")
    
    
    def complete_order(self, player_input):
        if not self.current_order:
            print (f"No orders")
            return 0
    
        crop = self.current_order["crop"]
        asked_qty = self.current_order["quantity"]
        total = self.current_order["total"]
    
        correct_qty = player_input.count(crop)
    
        if correct_qty >= asked_qty:
            self.bank_balance += total
            print(f"Yayyyyy! Order Complete! You earned ${total}")
            self.current_order = None
            return total
        else:
            print(f"Order not completed :/)")
            return 0


    def new_level_crops(self):

        level_next_game = {
         "Level 2": FarmersBazaar.level2,
         "Level 3": FarmersBazaar.level3,
         "Level 4": FarmersBazaar.level4
         }

        bank_limit = {
            2: 30,
            3: 45,
            4: 60}
            
        for level, threshold in bank_limit.items():
            if self.bank_balance >= threshold and level not in self.unlocked_levels:
                self.unlocked_levels.add(level)
                print(f"Yayyyy! Level {level} unlocked!")
        
                new_crops = list(level_next_game[level].keys())
                for crop in new_crops:
                    if crop not in self.crop_list:
                        self.crop_list.append(crop)
                print (f"Yayyyy! New crops: {new_crops} unlocked!")
   
    def upgrade(self):
        daily_tasks = FarmersBazaar.daily_task
        need_tasks = daily_tasks.get(self.player_level,[])

        for task in need_tasks:
            if task not in self.completed_tasks:
                return self.player_level, [], {"finish all the task to level up"}
    
        self.player_level +=1
        tasks_unlock = daily_tasks.get(self.player_level,[])
    
        rewards = {}
        if 1<= self.player_level <= 4:
            rewards["starter_kit"] = True
        elif 5 <= self.player_level <= 9:
            rewards["upgrade_crops"] = True
        else: 
            rewards["premium_market"] = True
        
        return self.player_level, tasks_unlock, rewards
    
    def beginning(self):
        print("""🐝 🍄 🌿 Hello Farmer, welcome to our game Farmer's Bazaar! 🌿 🍄 🐝""")
        print("""
              \nAre you ready to embark on the jouney of growing, harvesting, selling, and spreading joy to your customers?
              \n🍉 🌽 🍇 🍓 🫐 🍰 🥕 🥦 🍞 🍎 🍉 🌽 🍇 🍓 🫐 🍰 🥕 🥦 🍞 🍎 🍉 🌽 🍇 🍓 🫐 🍰 🥕 🥦 🍞 🍎 🍉 🌽 🍇 🍓 🫐 🍰 🥕 
              \nIf you are, please type "I can grow!" """)
        while True: 
            first_message = input().strip()
            if first_message == "I can grow!":
                print("Great! Let's go!")
                break
            else:
                print("Please type 'I can grow!' in terminal to begin")

def main():
    game = FarmersBazaar()
    game.beginning()
    
    player_level = 1
    completed_tasks = ["watering", "fertilizing"]

    levels_in_game = {
        1: FarmersBazaar.level1,
        2: FarmersBazaar.level2,
        3: FarmersBazaar.level3,
        4: FarmersBazaar.level4
    }

    while True:
        print(f"\nCurrent Level: {player_level}")
        print(f"Total Bank Balance: ${game.bank_balance}")
        print(f"Total Customer Satisfaction: {game.customer_satisfaction:.2f}")

        crops_for_sale = levels_in_game[player_level]
        crop_names = list(crops_for_sale.keys())
        answers, on_time = game.timed(crop_names)

        earned, satisfaction = game.level_check_method(answers, crops_for_sale)
        print(f"Earned: ${earned}, Satisfaction: {satisfaction:.2f}")

        game.new_level_crops()

        player_level, tasks_unlock, rewards = game.upgrade()
        
        print("Upgraded Level:", player_level)
        print("Tasks to unlock:", tasks_unlock)
        print("Rewards:", rewards)
        
        cont = input("Do you want to play the next level? (yes/no): ").lower()
        if cont != "yes":
            print("Thanks for playing Farmer's Bazaar!")
            break


if __name__ == "__main__":
    main()
