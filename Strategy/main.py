from shopping_cart import ShoppingCart
from payment_strategy import CreditCardStrategy, PayPalStrategy

shop = ShoppingCart()
shop.add_item(item={"name": "soap", "price": 50})
shop.add_item(item={"name": "item2", "price": 50})
# print(shop.get_total())
res = shop.checkout(payment_strategy=CreditCardStrategy(card_number="123123123123213"))
print(res)

shop.add_item(item={"name": "soap", "price": 520})
shop.add_item(item={"name": "item2", "price": 50})


res = shop.checkout(payment_strategy=PayPalStrategy(email="raghul@gmail.com", secret="123123"))
print(res)

