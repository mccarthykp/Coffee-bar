from order import Order

class Person():
  def __init__(self, name, favorite_drink):
    self.name = name
    self.favorite_drink = favorite_drink

  def my_order(self):
    order = Order('Coffee', self.name)
    return order.to_string()

if __name__ == "__main__":
  Amy = Person('Amy', 'Coffee')
  Bob = Person('Bob', 'Tea')
  Cat = Person('Cat', 'Milk')

  print(Bob.my_order())
  