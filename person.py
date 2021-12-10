from order import Order

class Person():
  def __init__(self, name, favorite_drink, wallet):
    self.name = name
    self.favorite_drink = favorite_drink
    self.wallet = wallet

  def my_order(self):
    order = Order(self.favorite_drink, self.name)
    return order


if __name__ == "__main__":
  Amy = Person('Amy', 'Coffee')
  Bob = Person('Bob', 'Tea')
  Cat = Person('Cat', 'Milk')

  print(Bob.my_order().to_string())
  