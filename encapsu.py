class AccountHolder:
    
    def __init__(self):
        self.AccountHolder = 123456789
        self.__balance = 3456
        self.__password = 56577

    def set_password(self, p):
        self.__password = p

    def get_password(self):
        return self.__password

    def get_balance(self):
        return self.__balance


a = AccountHolder()

print(a.get_balance())

a.set_password(1234)
print(a.get_password()) 
