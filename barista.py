from person import Person

class Barista(Person):
  def __init__(self, name, favorite_drink, wallet, greeting):
    super().__init__(name, favorite_drink, wallet)
    self.greeting = greeting