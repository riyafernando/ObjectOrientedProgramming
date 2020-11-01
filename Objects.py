class Pet():
    '''represents a pet'''

    def __init__(self,name):
        '''Pet(name) -> Pet
        creates a pet with the given name'''
        self.name = name

    def __str__(self):
        '''str(Pet) -> str'''
        return "A pet named "+str(self.name)

    def feed(self):
        '''Pet.feed()
        feeds a pet'''
        print(self.name+' has been fed.')

    def play(self,other):
        '''Pet.play(Pet)
        two pets playing'''
        print(self.name+' is playing with '+other.name+'.')

class Dog(Pet):
    '''represents a dog'''

    def walk(self):
        '''Dog.walk()
        walks the dog'''
        print(self.name+' is enjoying a nice walk.')

    def speak(self):
        '''Dog.speak()
        makes the dog speak'''
        print(self.name+' says "Bark!".')

    def play(self,other):
        '''Dog.play(Pet)
        two pets playing'''
        if isinstance(other,Cat):
            print("Dogs and cats do NOT play together!")
        else:
            Pet.play(self,other)

class Cat(Pet):
    '''represents a cat'''

    def speak(self):
        '''Cat.speak()
        makes the cat speak'''
        print(self.name+' says "Meow!".')

    def play(self,other):
        '''Cat.play(Pet)
        two pets playing'''
        if isinstance(other,Dog):
            print("Dogs and cats do NOT play together!")
        else:
            Pet.play(self,other)

d = Dog('Rover')
f = Dog('Fido')
c = Cat('Bingo')
d.play(f)
d.play(c)





class BankAccount:
    '''represents a bank account'''

    def __init__(self,accountNum,bal):

        '''BankAccount(accountNum,bal) -> BankAccount
        creates a new bank account with the given account
          number and balance'''
        self.actNum = accountNum
        self.balance = bal

    def __str__(self):
        '''str(BankAccount) -> str'''
        return 'Account #{} with balance ${:.2f}'.format(self.actNum,self.balance)

    def check_funds(self,amt):
        '''BankAccount.check_funds(amt) -> boolean
        returns True if the balance is at least amt, False otherwise
        prints warning message if not enough funds'''
        if amt > self.balance:
            print('Not enough funds!')
            return False
        return True

    def deposit(self,amt):
        '''BankAcount.deposit(amt)
        adds amt to balance of account'''
        self.balance += amt

    def withdraw(self,amt):
        '''BankAccount.withdraw(amt)
        remove amt from balance of account
        does nothing and prints warning if insufficient funds'''
        if self.check_funds(amt):
            self.balance -= amt

    def transfer(self,other,amt):
        '''BankAccount.transfer(other,amt)
        transfers amt from account to other account
        does nothing and prints warning if insufficient funds'''
        if self.check_funds(amt):
            self.withdraw(amt)
            other.deposit(amt)

class CheckingAccount(BankAccount):
    '''represents a checking account'''

    def __init__(self,accountNum,bal):
        '''CheckingAccount(accountNum, bal) -> CheckingAccount
        creates a new checking account with the given account
          number and balance'''
        BankAccount.__init__(self,accountNum,bal)
        self.checks = {}

    def __str__(self):
        '''str(CheckingAccount) -> str'''
        return 'Checking '+BankAccount.__str__(self)

    def write_check(self,checkNum,payee,amt):
        '''CheckingAccount.write_check(checkNum,payee,amt)
        writes a check numbered checkNum to payee for amt
        prints an error message if the checkNum is already used
          or if insufficient funds'''
        if checkNum in self.checks:
            print('Check #'+str(checkNum)+' is already used!')
        elif self.check_funds(amt):
            self.checks[checkNum] = (payee,amt)
            self.withdraw(amt)

    def print_checks(self):
        '''CheckingAccount.print_checks()
        print the list of checks'''
        checksString = ''
        checkNumList = list(self.checks.keys())
        checkNumList.sort()
        for check in checkNumList:
            checksString += 'Check #{} to {}: ${:.2f}\n'.format(check, \
                            self.checks[check][0],self.checks[check][1])
        return checksString

class SavingsAccount(BankAccount):
    '''represents a savings account'''

    def __init__(self,accountNum,bal,intrate):
        '''SavingsAccount(accountNum,bal,intrate) -> SavingsAccount
        creates a new savings account with the given account
          number, balance, and interest rate.'''
        BankAccount.__init__(self,accountNum,bal)
        self.interestRate = intrate

    def __str__(self):
        '''str(SavingsAccount) -> str'''
        return 'Savings '+BankAccount.__str__(self)

    def earn_interest(self):
        '''SavingsAccount.earn_interest(self)
        adds interest to account'''
        self.balance += (self.balance * self.interestRate)

class MoneyMarketAccount(CheckingAccount,SavingsAccount):
    '''represents a money market account'''

    def __init__(self,accountNum,bal,intrate):
        '''MoneyMarketAccount(accountNum,bal,intrate) -> MoneyMarketAccount
        creates a new savings account with the given account
          number, balance, and interest rate.'''
        SavingsAccount.__init__(self,accountNum,bal,intrate)
        self.checks = {}

    def __str__(self):
        '''str(MoneyMarketAccount) -> str'''
        return 'Money Market '+BankAccount.__str__(self)


# tests
c = CheckingAccount(1234,1000)
s = SavingsAccount(5678,2000,0.02)
c.write_check(100,'Dave',75)
c.write_check(102,'Tina',110)
c.transfer(s,200)
print(c)
print(c.print_checks())
print(s)
s.earn_interest()
print(s)













