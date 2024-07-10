import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

def start(store):
    while True:
        print("\nMenu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Option to list all products in the store
            all_products = store.get_all_products()
            for product in all_products:
                print(product.show())
        elif choice == "2":
            # Option to show total sum of all quantities in the store
            total_quantity = sum(product.quantity for product in store.get_all_products())
            print(f"Total quantity in store: {total_quantity}")
        elif choice == "3":
            # Option to make an order
            shopping_list = []
            while True:
                # Display available products for selection
                products = store.get_all_products()  # Re-fetch the product list to show updated quantities
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
                    # Attempt to buy the specified quantity of the selected product
                    products[product_index].buy(quantity)
                    shopping_list.append((products[product_index], quantity))
                    print(f"{quantity} {products[product_index].name}(s) added to the shopping list.")
                except ValueError as e:
                    # Handle case where quantity exceeds available stock
                    print(f"Error: {e}")
                    continue

            # Calculate and display total price for the order
            total_price = sum(product.price * quantity for product, quantity in shopping_list)
            print(f"Total price for the order: {total_price} dollars")
        elif choice == "4":
            # Quit the program
            print("Quitting...")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start(best_buy)
