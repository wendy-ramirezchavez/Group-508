def new_order(self, crop_order):
    crop = random.choice(list(crop_order.keys()))
    quantity = random.randit(2, 4)
    total = quantity * (crop_order[crop]+1)
    self.current_order = {
        "crop" = crop,
        "quantity" = quantity
        "total" = total
            }
    print(f"Please fulfill! {quantity} {crop}. Total: ${total}")
    
    
def complete_order(self, player_input):
    if not self.current_order:
        print (f"No orders")
        return 0
    
    crop = self.current_order["crop"]
    qty_needed = self.current_order["quantity"]
    total = self.current_order["bonus"]
    
    correct_qty = player_input.count(crop)
    
    if correct_qty >= asked_qty:
        self.bank_balance += total
        print(f"Yayyyyy! Order Complete! You earned ${total}")
        self.current_order = None
        return total
    else:
        print(f"Order not completed :/)")
        return 0
