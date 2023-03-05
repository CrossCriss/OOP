from datetime import datetime
import pytz



class ColorsForPrint:
    WHITE = '\033[00m'
    GREEN = '\033[0;92m'
    RED = '\033[1;31m'


class Account(ColorsForPrint):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self.history.append([amount, 
                             self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'You spent {amount} money!')
            self.history.append([-amount, 
                             self._get_current_time()])

        else:
            print(f'{Account.RED} Not enough money {Account.WHITE}')

        self.show_balance()
    
    def show_balance(self):
        print(f'Your total balance - {self.__balance}')


    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = Account.GREEN
            else:
                transaction = 'withdraw'
                color = Account.RED
            print(f'{color} {amount} {Account.WHITE} {transaction} on {date}')

acc = Account("Slava", 0)
acc.show_balance()
acc.deposit(100)
acc.withdraw(50)
acc.withdraw(60)
acc.show_history()
acc.__balance = 1000
acc.show_balance()