class Order():
  def __init__(self, drink_type, person):
    self.drink_type = drink_type
    self.person = person

  def to_string(self):
    order_string = f'{self.person.name} orders: {self.drink_type}'
    return order_string