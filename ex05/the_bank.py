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
    @classmethod
    @abstractmethod
    def inspect(cls, account : Account) -> bool:
        pass

class Right_account_inspector(Security):
    @classmethod
    def inspect(cls, account: Account) -> bool:
        return isinstance(account, Account)

class Corrupt_account_inspector(Security):
    MANDATORY_ATTRS = ['name', 'id', 'value']

    @classmethod
    def inspect(cls, account: Account) -> bool:
        try:
            checkers = [cls.check_attr_type, cls.check_attr_len, cls.check_attr_name, cls.check_mandatory_attr, cls.check_attr_key_validity]
            if all(check(account) == True for check in checkers) == True:
                return True
        except:
            return False

    @classmethod
    def check_attr_type(cls, account : Account):
        if isinstance(account.name, str) == False:
            raise AccountCorruptionException
        if isinstance(account.id, int) == False:
            raise AccountCorruptionException
        if isinstance(account.value, int) == False and isinstance(account.value, float) == False:
            raise AccountCorruptionException
        return True

    @classmethod
    def check_attr_len(cls, account : Account):
        if isEven(len(account.__dict__) % 2) == True:
            raise AccountCorruptionException
        return True
    
    @classmethod
    def check_attr_name(cls, account : Account):
        for key in account.__dict__.keys():
            if key.startswith("zip") == True or key.startswith('addr') == True:
                return True
        raise AccountCorruptionException
    
    @classmethod
    def check_mandatory_attr(cls, account : Account):
        if all(account.__dict__.__contains__(i) for i in cls.MANDATORY_ATTRS) == False:
            raise AccountCorruptionException
        return True
    
    @classmethod
    def check_attr_key_validity(cls, account : Account):
        for key, value in account.__dict__.items():
            if key.startswith("b") == True:
                raise AccountCorruptionException
        return True

class Balance_inspector(Security):
    @classmethod
    def inspect(cls, account: Account, amount : int or float) -> bool:
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
            if origin_account.widthrow(amount) == False:
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
            return True
        except:
            return False