from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, cc_no, exp_date, cvv):
        self.cc_no = cc_no
        self.exp_date = exp_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Processing credit card payment of Rs {amount}/-")
        print(f"Card Number: {self.cc_no}")
        print(f"Expiration Date: {self.exp_date}")
        print(f"CVV: {self.cvv}")

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Processing PayPal payment of Rs{amount}/-")
        print(f"PayPal Email: {self.email}")

class Bitcoin(PaymentMethod):
    def __init__(self, wallet_add):
        self.wallet_add = wallet_add

    def pay(self, amount):
        print(f"Processing Bitcoin payment of Rs {amount}/-")
        print(f"Wallet Address: {self.wallet_add}")

if __name__ == "__main__":
    credit_card = CreditCard(cc_no="1234-5678-8765-4321", exp_date="15/09/2025", cvv="123")
    paypal = PayPal(email="abcd@gmail.com.com")
    bitcoin = Bitcoin(wallet_add="3uirurguw3uru2rh23ri")

    credit_card.pay(1000.0)
    paypal.pay(2000.0)
    bitcoin.pay(3000.0)
