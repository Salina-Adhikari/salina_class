class Vehicle():

    def drive(self):
        print("Vehicle is driving")
    
    def new_fn(self):
        print("my new fn")

class Car(Vehicle):
    pass
car=Car()
print(car.drive())

class BankAccount:
    def __init__(self,name):
        self._balance=0
        self.name=name
    def deposit(self,amount):
        self._balance+=amount
    def withdraw(self,amount):
        self._balance-=amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f"Name:{self.name} and Balance:Hidden"
    
salina=BankAccount("Salina")
salina.deposit(10000)
print(salina)
print(salina.get_balance)
salina.withdraw(100)
salina.deposit(500)
salina.withdraw(600)
print(salina.get_balance())