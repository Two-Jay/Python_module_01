from abc import ABCMeta, abstractmethod

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
    
        if not hasattr(self, 'value'):
            self.value = 0
    
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount : int or float) -> bool:
        self.value += amount
        return True

    def widthrow(self, amount : int or float) -> bool:
        if Balance_inspector.inspect(self, amount) == True:
            self.value -= amount
            return True
        else:
            return False

    def isEnough(self, amount : int or float) -> bool:
        return self.value >= amount

class AccountCorruptionException(Exception):
    def __init__(self):
        pass

class Security(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def inspect(self, account : Account) -> bool:
        pass

class Right_account_inspector(Security):
    def inspect(self, account: Account) -> bool:
        return isinstance(account, Account)

class Corrupt_account_inspector(Security):
    MANDATORY_ATTRS = ['name', 'id', 'value']

    def inspect(self, account: Account) -> bool:
        try:
            if isEven(len(account.__dict__) % 2) == True:
                raise AccountCorruptionException
            if all(account.__dict__.__contains__(i) for i in self.MANDATORY_ATTRS) == False:
                raise AccountCorruptionException
            if type(account.__dict__['name']) != str:
                raise AccountCorruptionException
            if type(account.__dict__['id']) != int:
                raise AccountCorruptionException
            if type(account.__dict__['value']) != int and type(account.__dict__['value']) != float:
                raise AccountCorruptionException
            if any((key.startswith("zip") and key.startswith("addr")) == False for key in self.__dict__.keys()):
                raise AccountCorruptionException
            for key, value in account.__dict__.items():
                print(f"{key} - {value}")
                if key.startswith("b") == True:
                    raise AccountCorruptionException
            return True
        except:
            return False
    
class Balance_inspector(Security):
    def inspect(self, account: Account, amount) -> bool:
        return account.isEnough(amount)

def isEven(number : int) -> bool:
    return number % 2 == 0

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = Account_storage()

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code  ...
        try:
            Corrupt_account_inspector.inspect(new_account)
            self.accounts.create(new_account)
            return True
        except:
            return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        # ... Your code  ...
        try:
            Corrupt_account_inspector.inspect(origin)
            Corrupt_account_inspector.inspect(dest)
            origin_account = self.accounts.find_by_name(origin)
            dest_account = self.accounts.find_by_name(dest)
            if origin_account.widthrow(amount) == False
                raise Exception
            dest_account.transfer(amount)
            return True
        except:
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        # ... Your code  ...
        pass

class Account_storage():
    def __init__(self):
        self.storage = []
    
    def find_by_name(self, name : str) -> Account:
        for account in self.storage:
            if account.name == name:
                return account
        return None
    
    def create(self, account : Account) -> bool:
        self.storage.append(account)
        return True
    
    def remove(self, account : Account) -> bool:
        try:
            self.storage.remove(account)
        except:
            return False
        return True