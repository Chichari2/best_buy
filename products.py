class Product:
  def __init__(self, name, price, quantity):
    if not name or price < 0 or quantity < 0:
      raise ValueError("Invalid product details")
    self.name = name
    self.price = price
    self.quantity = quantity
    self.active = True
    self.promotion = None

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

  def set_promotion(self, promotion):
    self.promotion = promotion

  def get_promotion(self):
    return self.promotion

  def show(self):
    promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

  def buy(self, quantity):
    if quantity <= 0:
      raise ValueError("Quantity must be greater than zero")
    if quantity > self.quantity:
      raise ValueError("Not enough quantity available")
    if self.promotion:
      total_price = self.promotion.apply_promotion(self, quantity)
    else:
      total_price = quantity * self.price
    self.set_quantity(self.quantity - quantity)
    return total_price


class NonStockedProduct(Product):
  def __init__(self, name, price):
    super().__init__(name, price, quantity=0)

  def set_quantity(self, quantity):
    raise ValueError("Cannot set quantity for non-stocked products")

  def buy(self, quantity):
    if quantity <= 0:
      raise ValueError("Quantity must be greater than zero")
    return quantity * self.price

  def show(self):
    return f"{self.name}, Price: {self.price}, Quantity: Not applicable (non-stocked)"


class LimitedProduct(Product):
  def __init__(self, name, price, quantity, maximum):
    super().__init__(name, price, quantity)
    self.maximum = maximum

  def buy(self, quantity):
    if quantity <= 0:
      raise ValueError("Quantity must be greater than zero")
    if quantity > self.maximum:
      raise ValueError(f"Cannot buy more than {self.maximum} of {self.name}")
    return super().buy(quantity)

  def show(self):
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
