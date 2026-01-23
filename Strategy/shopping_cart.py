from payment_strategy import PaymentStrategy

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total
    
    def add_item(self, item):
        self.items.append(item)
    
    def checkout(self, payment_strategy: PaymentStrategy):
        total = self.get_total()
        return payment_strategy.pay(amount=total)

