
# * import
# ---------------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod


# * utils
# ---------------------------------------------------------------------------------
def isEven(number : int) -> bool:
    return number % 2 == 0

def isFloatNumeric(nbr : str) -> bool:
    try:
        float(nbr)
        return True
    except ValueError:
        return False

# * class Account
# ---------------------------------------------------------------------------------
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

# * class AccountCorruptionException
# ---------------------------------------------------------------------------------
class AccountCorruptionException(Exception):
    def __init__(self, message):
        self.message = message

# * Security classes
# ---------------------------------------------------------------------------------
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
            raise AccountCorruptionException("Attribute name must be a str object.")
        if isinstance(account.id, int) == False:
            raise AccountCorruptionException("Attribute id must be an int object.")
        if isinstance(account.value, int) == False and isinstance(account.value, float) == False:
            raise AccountCorruptionException("Attribute value must be an int or float object.")
        return True

    @classmethod
    def check_attr_len(cls, account : Account):
        if isEven(len(account.__dict__) % 2) == True:
            raise AccountCorruptionException("Attribute length is not even.")
        return True
    
    @classmethod
    def check_attr_name(cls, account : Account):
        for key in account.__dict__.keys():
            if key.startswith("zip") == True or key.startswith('addr') == True:
                return True
        raise AccountCorruptionException("Attribute must contain zip or addr.")
    
    @classmethod
    def check_mandatory_attr(cls, account : Account):
        if any(account.__dict__.__contains__(i) == False for i in cls.MANDATORY_ATTRS) == True:
            raise AccountCorruptionException("Mandatory attributes are missing.")
        return True
    
    @classmethod
    def check_attr_key_validity(cls, account : Account):
        for key, value in account.__dict__.items():
            if key.startswith("b") == True:
                raise AccountCorruptionException("Attribute key is invalid.")
        return True

class Balance_inspector(Security):
    @classmethod
    def inspect(cls, account: Account, amount : int or float) -> bool:
        return account.isEnough(amount)

# * class Account_Fixer
# ---------------------------------------------------------------------------------
class Account_Fixer(object):
    @classmethod
    def fix(cls, account : Account):
        if Corrupt_account_inspector.inspect(account) == True:
            return False
        fixers = [cls.fix_mandatory_attr, cls.fix_attr_type, cls.fix_attr_key_validity, cls.fix_attr_name, cls.fix_attr_len]
        for fixer in fixers:
            fixer(account)
        return True

    @classmethod
    def fix_attr_key_validity(cls, account : Account):
        try:
            Corrupt_account_inspector.check_attr_key_validity(account)
        except:
            for key, value in account.__dict__.items():
                if key.startswith("b") == True:
                    tmp = account.__dict__[key]
                    account.__dict__.pop(key)
                    account.__dict__["fixed_" + key[1:]] = tmp
            return True
    
    @classmethod
    def fix_attr_name(cls, account : Account):
        try:
            Corrupt_account_inspector.check_attr_name(account)
        except:
            account.__dict__['addr'] = 'unknown'

    @classmethod
    def fix_attr_len(cls, account : Account):
        try:
            Corrupt_account_inspector.check_attr_len(account)
        except:
            account.__dict__['fixed'] = 'unknown'
    
    @classmethod
    def fix_mandatory_attr(cls, account : Account):
        try:
            Corrupt_account_inspector.check_mandatory_attr(account)
        except:
            if account.__dict__.__contains__('name') == False:
                account.__dict__['name'] = 'unknown'
            if account.__dict__.__contains__('id') == False:
                account.__dict__['id'] = Account.ID_COUNT
                Account.ID_COUNT += 1
            if account.__dict__.__contains__('value') == False:
                account.__dict__['value'] = float(0.0)
    
    @classmethod
    def fix_attr_type(cls, account : Account):
        try:
            Corrupt_account_inspector.check_attr_type(account)
        except:
            if isinstance(account.name, str) == False:
                account.__dict__.pop('name')
                account.__dict__['name'] = 'unknown'
            if isinstance(account.id, int) == False:
                account.__dict__.pop('id')
                account.__dict__['id'] = Account.ID_COUNT
                Account.ID_COUNT += 1
            if isinstance(account.value, int) == False and isinstance(account.value, float) == False:
                tmp = account.__dict__.pop('value')
                if tmp.isnumeric() == True or isFloatNumeric(tmp) == True:
                    account.__dict__['value'] = float(tmp)
                else:
                    account.__dict__['value'] = float(0.0)

# * class Bank
# ---------------------------------------------------------------------------------
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
        if Corrupt_account_inspector.inspect(new_account) == True:
            self.accounts.create(new_account)
            return True
        else:
            return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        check_arg_type_list = [isinstance(origin, str), isinstance(dest, str), isinstance(amount, int) or isinstance(amount, float)]
        if all(check_arg_type_list) == False:
            return False

        origin_account = self.accounts.find_by_name(origin)
        dest_account = self.accounts.find_by_name(dest)
        if origin_account == None or dest_account == None:
            return False
        
        if Corrupt_account_inspector.inspect(origin_account) == False \
            or Corrupt_account_inspector.inspect(dest_account) == False:
            return False

        if Balance_inspector.inspect(origin_account, amount) == False:
            return False
        
        origin_account.widthrow(amount)
        dest_account.transfer(amount)
        return True

    def fix_account(self, name):
        """ Fix the account name
            @name:    str(name) of the account to fix
            @return   True if success, False if an error occured
        """
        if isinstance(name, str) == False:
            return False
        
        found_account = self.accounts.find_by_name(name)
        if found_account == None:
            return False
        if Corrupt_account_inspector.inspect(found_account) == True:
            return True
        Account_Fixer.fix(found_account)
        return True

    def remove(self, name):
        if self.accounts.remove(self.accounts.find_by_name(name)) == True:
            return True
        return False
    
    def find_account(self, name):
        return self.accounts.find_by_name(name)
        
    def print(self):
        for account in self.accounts.storage:
            print(account.__dict__)

# * class Account_storage
# ---------------------------------------------------------------------------------
class Account_storage():
    def __init__(self):
        self.storage = {}
    
    def find_by_name(self, name : str) -> Account:
        return self.storage.get(name)
    
    def create(self, account : Account) -> bool:
        self.storage[account.name] = account
        return True
    
    def remove(self, account : Account) -> bool:
        if self.storage.pop(account.name) == None:
            return False
        return True