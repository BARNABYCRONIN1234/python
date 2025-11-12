class BankAccount:
    #constructuctor for the bank class
    def __init__(self, name, balance):
        self.name = name
        #this is a private variable, can only
        self.__balance = balance
        
        def__str__(self):
        return f"{self.name} has balance {self.__balance}"

    #its a function to withdraw money, checks if you have enough money to widthdraw inthe 1st place
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print
        else:
            print("insufficient balance")
        print(f"£ {self.__balance}")

#depostit money into your bank account
    def deposit(self, amount):
        self.__balance += amount
        print(f"amount deposited {amount}")
        print(f"new balance -> {self.__balance}")

    #this is a getter method to access the value of the private variable __balance
    # can only be seen via this function
    def getBalance(self):
        return self.__balance
    
    #this is a setter method to change the value of the private variable __balance
    #can only be changed via this function
    def setBalance(self, balance):
        self.__balance = balance
        return self.__balance
    

    BankAccount1 = BankAccount("barnaby", 100)
    print(BankAccount)