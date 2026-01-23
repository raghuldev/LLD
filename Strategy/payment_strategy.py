from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def getPaymentDetails(self):
        pass


class CreditCardStrategy(PaymentStrategy):
    
    def __init__(self, card_number):
        self.card_number = card_number
        
    def pay(self, amount):
        return f"Credit Card Payment of amount {amount} successful using card {self.card_number}"
    
    def getPaymentDetails(self):
        print(f"Card Details:")
        print(f"Number: {self.card_number}")
    

class PayPalStrategy(PaymentStrategy):

    def __init__(self, email, secret):
        self.email = email
        self.secret = secret
    
    def pay(self, amount):
        return f"Paypal Payment of amount {amount} successful using email {self.email}"
    
    def getPaymentDetails(self):
        print(f"Email: {self.email}")

        