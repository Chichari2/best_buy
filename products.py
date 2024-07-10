class Product:

  def __init__(self, name, price, quantity):
    if not name or price < 0 or quantity < 0:
      raise ValueError("Invalid product details")
    self.name = name
    self.price = price
    self.quantity = quantity
    self.active = True

  def get_quantity(self):
    return self.quantity

  def set_quantity(self, quantity):
    if quantity < 0:
      raise ValueError("Quantity cannot be negative")
    self.quantity = quantity
    if self.quantity == 0:
      self.deactivate()

  def is_active(self):
    return self.active

  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False

  def show(self):
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

  def buy(self, quantity):
    if quantity <= 0:
      raise ValueError("Quantity must be greater than zero")
    if quantity > self.quantity:
      raise ValueError("Not enough quantity available")
    total_price = quantity*self.price
    self.set_quantity(self.quantity - quantity)
    return total_price




bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
mac.show()

bose.set_quantity(1000)
print(bose.show())


