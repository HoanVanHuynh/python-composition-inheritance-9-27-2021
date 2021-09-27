from compo import Person, Teller, Manager 

class Customer:
    def __init__(self,name):
        self.name = name 
    def transaction(self, teller):
        print(self.name, "is helped with a transaction from", teller)
    def mortgage(self, manager):
        print(self.name, "is helped with a mortgage from", manager)

class ATM:
    def giveMoney(self):
        print("Here's some money") 

class Bank:
    def __init__(self):
        self.manager = Manager('Joe') 
        self.teller = Teller('Judy') 
        self.atm = ATM() 
    
    def transaction(self, name):
        customer = Customer(name) 
        customer.transaction(self.teller) 
        self.atm.giveMoney() 
    
    def mortgage(self, name):
        customer2 = Customer(name)
        customer2.mortgage(self.manager)

if __name__ == '__main__':
    b = Bank() 
    b.transaction('John') 
    b.mortgage('Miles') 
    