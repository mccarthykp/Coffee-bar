from barista import Barista
from person import Person

class CoffeeBar():
  def __init__(self, name, barista):
    self.name = name
    self.order_list = []
    self.barista = barista

  def place_order(self, order):
    self.order_list.append(order)

  def process_orders(self):
    print(self.barista.greeting)
    for order in self.order_list:
      print(order.to_string())


if __name__ == "__main__":
  Amy = Person('Amy', 'Coffee')
  Bob = Person('Bob', 'Tea')
  Cat = Person('Cat', 'Milk')
  Kevin = Barista('Kevin', 'Cold Brew', 'Hey dude!')
  CoffeeEmporium = CoffeeBar('Coffee Emporium', Kevin)

  CoffeeEmporium.place_order(Amy.my_order())
  CoffeeEmporium.place_order(Bob.my_order())
  CoffeeEmporium.place_order(Cat.my_order())

  CoffeeEmporium.process_orders()