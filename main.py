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

# Testing the products
for product in best_buy.get_all_products():
    print(product.show())

# Attempt to buy products with promotions
print(product_list[0].buy(3))  # Should apply second half price promotion
print(product_list[1].buy(3))  # Should apply third one free promotion
print(product_list[3].buy(2))  # Should apply 30% discount promotion
