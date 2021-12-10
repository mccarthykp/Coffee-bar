class CoffeeBar():
  def __init__(self, name):
    self.name = name
    self.order_list = []

  def place_order(self, order):
    self.order_list.append(order)

  def process_orders(self):
    for order in self.order_list:
      print(order.to_string())