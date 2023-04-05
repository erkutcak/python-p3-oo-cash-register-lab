#!/usr/bin/env python3

# CashRegister in cash_register.py subtracts the last item from the total F                                                                        [ 92%]
# CashRegister in cash_register.py returns the total to 0.0 if all items have been removed F 

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.prev_total = 0
    self.items = []
  
  def add_item(self, title, price, quantity = 1):
    self.prev_total = price * quantity
    self.total += self.prev_total
    for _ in range(quantity):
      self.items.append(title)
  
  def apply_discount(self):
    if (self.discount > 0):
      self.total -= int(self.total * self.discount / 100)
      print (f"After the discount, the total comes to ${self.total}.")
    else:
      print('There is no discount to apply.')
  
  def void_last_transaction(self):
    self.total -= self.prev_total
