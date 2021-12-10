from person import Person

class CoffeeBar():
  def __init__(self, name):
    self.name = name
    self.order_list = []

  def place_order(self, order):
    self.order_list.append(order)

  def process_orders(self):
    for order in self.order_list:
      print(order.to_string())


if __name__ == "__main__":
  Amy = Person('Amy', 'Coffee')
  Bob = Person('Bob', 'Tea')
  Cat = Person('Cat', 'Milk')
  CoffeeEmporium = CoffeeBar('Coffee Emporium')

  CoffeeEmporium.place_order(Amy.my_order())
  CoffeeEmporium.place_order(Bob.my_order())
  CoffeeEmporium.place_order(Cat.my_order())

  CoffeeEmporium.process_orders()