import products
class Store:

  def __init__(self, list_of_products):
    self.list_of_products = list_of_products

  def add_product(self, product):
    self.list_of_products.append(product)

  def remove_product(self, product):
    self.list_of_products.remove(product)

  def get_total_quantity(self):
    total_quantity = 0
    for _ in self.list_of_products:
      total_quantity += 1
    return total_quantity

  def get_all_products(self):
    list_of_active_products = []
    for product in self.list_of_products:
      if product.is_active() == True:
        list_of_active_products.append(product)
    return list_of_active_products

  def order(self, shopping_list):
    total_price = 0.0
    for item in shopping_list:
      product, quantity = item
      total_price += product.buy(quantity)
    return total_price


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))