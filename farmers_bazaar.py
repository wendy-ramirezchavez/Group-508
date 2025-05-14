import time
import timeit
import random

class FarmersBazaar():
    """
    Farmers Bazaar is your virtual farmers market game. Players are able 
    to sell crops, fulfill orders, and maintain customer satisfaction in order to 
    earn rewards and money.
    
    Attributes:
        level1 (dict): crops and price for level 1
        level2 (dict): crops and price for level 2
        level3 (dict): crops and price for level 3
        level4 (dict): crops and price for level 4
        daily_tasks (dict): daily tasks for level up in each level
        customer_satisfaction (float): customer statisfaction
        bank_balance (int): players total money
        crop_list (list): List of available crops
        unlocked_levels: set of unlocked level
        player_level (int): players level
        complete_tasks (list): list of completed daily task
        current_order: order needed to be fulfilled
    """
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
    characters = {
    "Maru": {
        "specialty": "Technology and carpenting",
        "bonus": 5,
     
    },
    "Penny": {
        "specialty": "Education and reading",
        "bonus_satisfaction": 1.1,
      
    },
    "Clint": {
        "specialty": "Crafts and building ",
        "bonus_crop": True,
    
    }
    }
    
    def __init__(self, character_name):
        """
        Initializes the game with intial customer_satisfaction, bank_balance, and player levels
        """
        self.customer_satisfaction = 1.0
        self.bank_balance = 0
        self.crop_list = list(FarmersBazaar.level1.keys())
        self.unlocked_levels = {1}
        self.player_level = 1
        self.completed_tasks = ["watering", "fertilizing"]
        self.current_order = None
        self.character = character_name
        
        character_data = FarmersBazaar.characters.get(character_name, {})
        self.bank_balance += character_data.get("bonus_amount", 0)
        self.customer_satisfaction = character_data.get("bonus_satisfaction", self.customer_satisfaction)
        
        if character_data.get("bonus_crop"):
            extra_crop = random.choice(["spinach", "radish", "turnip"])
            self.crop_list.append(extra_crop)
            print(f"Bonus Crop Unlocked: {extra_crop}")




    def level_check_method(self,user_input, crops_for_sale): 
        """
        sums total earned money and adds it to the bank balance as well 
        as ensures crops typed matches the list
        
        Args:
            user_input (list): list of crops player types
            crops_for_sale (dict): dictionary of crop at current level

        Returns:
            tuple: total eaned and customer satisfaction
        """
        bank = []
        correct = set(user_input) & set(crops_for_sale)
        for crop in correct:
            bank.append(crops_for_sale[crop])
        self.bank_balance += sum(bank)
        self.customer_satisfaction -= len(set(user_input) ^ set(crops_for_sale)) * 0.10
        return sum(bank), self.customer_satisfaction
    
    def memory_block (self, crops_for_sale):
        print('You are getting ready for a farmers market! How exciting!')
        print("Before the farmers market, you must remember to bring all of your crops.")
        print(f'For this farmers market, you must bring the following, {crops_for_sale}.')
        print("Once you have memorized the crops you must bring to the market, please type 'I am ready'.")
        
        while True: 
            remember_message = input().strip()
            if remember_message == "I am ready":
                print("""
░██████╗███████╗████████╗████████╗██╗███╗░░██╗░██████╗░  ██╗░░░██╗██████╗░  ░█████╗░████████╗
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗░██║██╔════╝░  ██║░░░██║██╔══██╗  ██╔══██╗╚══██╔══╝
╚█████╗░█████╗░░░░░██║░░░░░░██║░░░██║██╔██╗██║██║░░██╗░  ██║░░░██║██████╔╝  ███████║░░░██║░░░
░╚═══██╗██╔══╝░░░░░██║░░░░░░██║░░░██║██║╚████║██║░░╚██╗  ██║░░░██║██╔═══╝░  ██╔══██║░░░██║░░░
██████╔╝███████╗░░░██║░░░░░░██║░░░██║██║░╚███║╚██████╔╝  ╚██████╔╝██║░░░░░  ██║░░██║░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═╝░░░░░  ╚═╝░░╚═╝░░░╚═╝░░░

████████╗██╗░░██╗███████╗  ███╗░░░███╗░█████╗░██████╗░██╗░░██╗███████╗████████╗░░░░░░░░░░░░
╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝░░░░░░░░░░░░
░░░██║░░░███████║█████╗░░  ██╔████╔██║███████║██████╔╝█████═╝░█████╗░░░░░██║░░░░░░░░░░░░░░░
░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░██╔══╝░░░░░██║░░░░░░░░░░░░░░░
░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗███████╗░░░██║░░░██╗██╗██╗██╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝╚═╝╚═╝╚═╝
\n
\n 🍉 🌽 🍇 🍓 🫐 🍰 🥕 🥦 🍞 🍎 🍉 🌽 🍇 🍓 🫐 🍰 🥕 🥦 🍞 🍎 🍉 🌽 🍇 🍓 🫐 🍰 🥕 🥦 🍞 🍎 🍉 🌽 🍇 🍓 🫐 🍰 🥕
\n
\n
████████╗██╗░░██╗███████╗  ███████╗░█████╗░██████╗░███╗░░░███╗███████╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║██╔════╝██╔══██╗
░░░██║░░░███████║█████╗░░  █████╗░░███████║██████╔╝██╔████╔██║█████╗░░██████╔╝
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║███████╗  ██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝

████████╗██╗░░██╗██╗███╗░░██╗██╗░░██╗░██████╗██╗  ██╗██╗██╗  ██╗░░██╗░█████╗░██████╗░███████╗
╚══██╔══╝██║░░██║██║████╗░██║██║░██╔╝██╔════╝╚═╝  ╚█║╚█║██║  ██║░░██║██╔══██╗██╔══██╗██╔════╝
░░░██║░░░███████║██║██╔██╗██║█████═╝░╚█████╗░░░░  ░╚╝░╚╝██║  ███████║██║░░██║██████╔╝█████╗░░
░░░██║░░░██╔══██║██║██║╚████║██╔═██╗░░╚═══██╗░░░  ░░░░░░██║  ██╔══██║██║░░██║██╔═══╝░██╔══╝░░
░░░██║░░░██║░░██║██║██║░╚███║██║░╚██╗██████╔╝██╗  ░░░░░░██║  ██║░░██║╚█████╔╝██║░░░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚═╝  ░░░░░░╚═╝  ╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝

██╗  ░█████╗░░█████╗░███╗░░██╗  ██████╗░███████╗███╗░░░███╗███████╗███╗░░░███╗██████╗░███████╗██████╗░
██║  ██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔════╝████╗░████║██╔════╝████╗░████║██╔══██╗██╔════╝██╔══██╗
██║  ██║░░╚═╝███████║██╔██╗██║  ██████╔╝█████╗░░██╔████╔██║█████╗░░██╔████╔██║██████╦╝█████╗░░██████╔╝
██║  ██║░░██╗██╔══██║██║╚████║  ██╔══██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║  ╚█████╔╝██║░░██║██║░╚███║  ██║░░██║███████╗██║░╚═╝░██║███████╗██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

░█████╗░██╗░░░░░██╗░░░░░  ░█████╗░███████╗  ███╗░░░███╗██╗░░░██╗
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔════╝  ████╗░████║╚██╗░██╔╝
███████║██║░░░░░██║░░░░░  ██║░░██║█████╗░░  ██╔████╔██║░╚████╔╝░
██╔══██║██║░░░░░██║░░░░░  ██║░░██║██╔══╝░░  ██║╚██╔╝██║░░╚██╔╝░░
██║░░██║███████╗███████╗  ╚█████╔╝██║░░░░░  ██║░╚═╝░██║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚══════╝  ░╚════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗░█████╗░████████╗░██████╗░░░░░░░░░██╗██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██╔════╝░░░░░░░░░╚█║╚█║
██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║██║░░╚═╝░░░██║░░░╚█████╗░░░░░░░░░░░╚╝░╚╝
██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║██║░░██╗░░░██║░░░░╚═══██╗░░░░░░░░░░░░░░░
██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝╚█████╔╝░░░██║░░░██████╔╝██╗██╗██╗░░░░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░╚═╝╚═╝╚═╝░░░░░░""")
                break
            else:
                ("Please type 'I am ready' in the terminal to head to the farmers bazaar.")

    def timed (self, crops):
        """
        Timer for player to ensure player types in the limited time given
        Args:
            crops (list): list of crops the player needs to type
        Returns:
            tuple: list of answers typed by the player
        """
        typed_crops = []
          
        print(f"You are asked to type the crops you are bringing to the farmers bazaar.")
        print("when you are finished, type 'done' ")
        print("Type all the words in time or else you lose.")
    
        start = time.time()
       
         
        while True:
         crop = input("Enter crop: ").lower().strip()
         if crop == "done":  
            break
         typed_crops.append(crop)
    
        end = time.time()
    
        duration = end - start
        print(duration)
        
        expected = set(c.lower().strip() for c in crops)
        typed_set = set(typed_crops)
    
        if duration < 30 and set(typed_crops) == expected:
           print("✅ You made it in time and typed all the correct crops!")
           return typed_crops, True

        elif duration < 30 and typed_set != expected:
            print(f"""\nYou forgot a crop to bring to the farmers market ({typed_set ^ expected}) your customers were not happy... 
                  \nkeep an eye on your decreasing customer satisfaction. """)
            self.customer_satisfaction -= 0.2
            return typed_crops, False
        else:
            print("You did not make it in time, your customers were not happy.")
            self.customer_satisfaction -= 0.2
            return typed_crops, False
        
    def new_order(self, crop_order):
        """
        creates a new random crop order for the player to fulfill
        Args:
            crop_order (dict): crops for sale
        """
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
        """
        checks if player completes order

        Args:
            player_input (list): players input on crops

        Returns:
            total (int): total amount of money added to bank balnce 
            from completeing order
        """
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
        """
        unlocks new lecels and crops based on new level unlocked
        """

        level_next_game = {
         2: FarmersBazaar.level2,
         3: FarmersBazaar.level3,
         4: FarmersBazaar.level4
         }

        bank_limit = {
            2: 15,
            3: 30,
            4: 45}
            
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
        """
        creates tasks to allow players to level up and gives players rewards after completing the tasks.
        """
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
        """
        Game introdutction to start up the game and greet player
        """
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
    """
    Main game function that runs the full program so players can go through
    levels, tasks, and earn money
    """
    
    print("Choose your character to begin your farming journey!")
    print("1. Maru (Tech genius and efficient)")
    print("2. Penny (Gentle and organized)")
    print("3. Clint ( Hardworking and strong)")

    character_options = {
        "1": "Maru",
        "2": "Penny",
        "3": "Clint"
    }
    while True:
        choice = input("Enter the number of your character choice (1/2/3): ").strip()
        if choice in character_options:
            character_name = character_options[choice]
            print(f"You have chosen {character_name}! 🌱")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
            
            
    game = FarmersBazaar(character_name)

    game.beginning()

    levels_in_game = {
        1: FarmersBazaar.level1,
        2: FarmersBazaar.level2,
        3: FarmersBazaar.level3,
        4: FarmersBazaar.level4
    }

    while True:
        print(f"\nCurrent Level: {game.player_level}")
        print(f"Total Bank Balance: ${game.bank_balance}")
        print(f"Total Customer Satisfaction: {game.customer_satisfaction:.2f}")

        crops_for_sale = levels_in_game[game.player_level]
        crop_names = list(crops_for_sale.keys())
        game.memory_block(list(crops_for_sale))
        answers, on_time = game.timed(crop_names)
        earned, satisfaction = game.level_check_method(answers, crops_for_sale)
        print(f"Earned: ${earned}, Satisfaction: {satisfaction:.2f}")

        game.new_level_crops()


        game.player_level, tasks_unlock, rewards = game.upgrade()
        
        print("Upgraded Level:", game.player_level)
        print("Tasks to unlock:", tasks_unlock)
        print("Rewards:", rewards)
        
        cont = input("Do you want to play the next level? (yes/no): ").lower()
        if cont != "yes":
            print("Thanks for playing Farmer's Bazaar!")
            break
        

if __name__ == "__main__":
    main()
