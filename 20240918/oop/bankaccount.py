#encapsulation

class Account:
    def __init__(self,number,name,initial_amount=1000):
        self.__name=name
        self.__number=number
        self.__balance=initial_amount
    def __repr__(self):
        return f'[number={self.__number},name={self.__name},balance={self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print('no enough balance')
            return
        self.__balance-=amount

charu_ac=Account(name='charulatha',number='9390723151',initial_amount=5000)
print(charu_ac)
charu_ac.deposit(20000)
print(charu_ac)
charu_ac.deposit(10000)
print(charu_ac)
charu_ac.withdraw(36000)
print(charu_ac)
#print(charu_ac.__dict__)
#print(charu_ac.__balance) get an error because the balance can not be shown to others
charu_ac.withdraw(3000)
print(charu_ac)