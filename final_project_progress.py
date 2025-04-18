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
        
if __name__ == "__main__":
    print(level_check_method(("potato","carrot","asparagus", "broccoli","corn"),level1, customer_satisfaction))
    

"""
user_input = list 
"""
    