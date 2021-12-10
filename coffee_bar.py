from barista import Barista
from person import Person

class CoffeeBar():
  def __init__(self, name, barista):
    self.name = name
    self.order_list = []
    self.barista = barista

    self.coffee = 2.50
    self.tea = 1.85
    self.milk = 1.25

  def place_order(self, order):
    self.order_list.append(order)

  def process_orders(self):
    print(self.barista.greeting)
    for order in self.order_list:
      print(order.to_string())

      if order.drink_type == 'Coffee':
        # error here -- order.person == str and not Object? 
        order.person.wallet -= self.milk

      # if order.drink_type == 'Coffee':
      #   print(order.person.wallet)
      #   # order.person.wallet -= self.coffee
      # elif order.drink_type == 'Tea':
      #   order.person.wallet -= self.tea
      # elif order.drink_type == 'Milk':
      #   order.person.wallet -= self.milk
  

if __name__ == "__main__":
  Amy = Person('Amy', 'Coffee', 10.00)
  Bob = Person('Bob', 'Tea', 3.50)
  Cat = Person('Cat', 'Milk', 8.75)
  Kevin = Barista('Kevin', 'Cold Brew', 100.00, 'Hey dude!')
  CoffeeEmporium = CoffeeBar('Coffee Emporium', Kevin)

  CoffeeEmporium.place_order(Amy.my_order())
  CoffeeEmporium.place_order(Bob.my_order())
  CoffeeEmporium.place_order(Cat.my_order())

  print(Cat.wallet)
  CoffeeEmporium.process_orders()
  print(Cat.wallet)