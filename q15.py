class Customer:
    def __init__(self, name ,address, balance):
        self.name = name
        self.address = address
        self.balance = balance

    def withdraw(self, withdraw_amt):
        self.balance = self.balance - withdraw_amt
        print(f"Rs. {withdraw_amt} has been withdrawn")
        print("Your remainging balance is {}". format(self.balance))

    def deposit(self, deposit_amt):
        self.balance = self.balance + deposit_amt
        print(f"{deposit_amt} has been deposited")
        print(f"Your new balance is {self.balance}")

cust = Customer('Nishan', 'Buyo', 10000)
cust.withdraw(100)

