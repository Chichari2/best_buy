import products
import store
import promotions

# setup initial stock of inventory
product_list = [
  products.Product("MacBook Air M2", price=1450, quantity=100),
  products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
  products.Product("Google Pixel 7", price=500, quantity=250),
  products.NonStockedProduct("Windows License", price=125),
  products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half Price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def display_menu():
  print("\nStore Menu")
  print("----------")
  print("1. List all products in store")
  print("2. Show total amount in store")
  print("3. Make an order")
  print("4. Quit")


def list_products():
  all_products = best_buy.get_all_products()
  for product in all_products:
    print(product.show())


def show_total_amount():
  total_quantity = best_buy.get_total_quantity()
  print(f"Total quantity in store: {total_quantity}")


def make_order():
  shopping_list = []
  while True:
    products = best_buy.get_all_products()
    print("\nAvailable products:")
    for idx, product in enumerate(products, start=1):
      print(f"{idx}. {product.show()}")

    product_number = input("Enter the product number (or 'done' to finish): ")
    if product_number.lower() == "done":
      break
    if not product_number.isdigit() or int(product_number) < 1 or int(product_number) > len(products):
      print("Invalid product number. Please try again.")
      continue
    product_index = int(product_number) - 1
    quantity = int(input(f"Enter the quantity for {products[product_index].name}: "))
    try:
      products[product_index].buy(quantity)
      shopping_list.append((products[product_index], quantity))
      print(f"{quantity} {products[product_index].name}(s) added to the shopping list.")
    except ValueError as e:
      print(f"Error: {e}")
      continue

  total_price = best_buy.order(shopping_list)
  print(f"Total price for the order: {total_price}")


def main():
  while True:
    display_menu()
    choice = input("Please choose a number: ")

    if choice == "1":
      list_products()
    elif choice == "2":
      show_total_amount()
    elif choice == "3":
      make_order()
    elif choice == "4":
      print("Quitting...")
      break
    else:
      print("Invalid choice. Please choose again.")


if __name__ == "__main__":
  main()
