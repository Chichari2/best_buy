import products


class Store:
  def __init__(self, list_of_products):
    self.list_of_products = list_of_products

  def add_product(self, product):
    self.list_of_products.append(product)

  def remove_product(self, product):
    self.list_of_products.remove(product)

  def get_total_quantity(self):
    return sum(product.quantity for product in self.list_of_products if product.is_active())

  def get_all_products(self):
    return [product for product in self.list_of_products if product.is_active()]

  def order(self, shopping_list):
    total_price = 0.0
    for item in shopping_list:
      product, quantity = item
      total_price += product.buy(quantity)
    return total_price
