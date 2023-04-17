# * import
# ---------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from textwrap import dedent
# * import End --------------------------------------------------------------------


# * utils
# ---------------------------------------------------------------------------------
def isEven(n : int) -> bool:
    return n % 2 == 0

def isFloatDigit(n : str) -> bool:
    try :
        float(n)
        return True
    except ValueError:
        return False
# * utils End --------------------------------------------------------------------


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
        if amount < 0:
            return False
        self.value += amount
        return True
    
    def withdraw(self, amount : int or float) -> bool:
        if self.value - amount < 0:
            return False
        self.value -= amount
        return True
    
    def isBalanced(self, amount : int or float) -> bool:
        return self.value >= amount
    
    def get_attr_len(self) -> int:
        return len(self.__dict__)

    def __str__(self):
        return f"Account #{self.id:05} - {self.name} : {self.value}"
# * class Account End -------------------------------------------------------------

# * classes for AccountCorruptionCondition ========================================

###
# - corruption of the account
#  - an even number of attributes
#  - an attribute starting with b
#  - no attribute starting with 'zip' or 'addr'
#  - no attribute 'name' and the 'name' attribute is not a string
#  - no attribute 'id' and the 'id' attribute is not an int
#  - no attribute 'value' and the 'value' attribute is not an int or a float
###

# * class AccountCorruptionConditionInterface(abstract)
# ---------------------------------------------------------------------------------
class AccountCorruptionConditionInterface(ABC):
    @abstractmethod
    def isCorrupted(self, account : Account) -> bool:
        pass
# * class AccountCorruptionCondition End ------------------------------------------


# * classes for Corruption Check : AccountCorruptionConditionInterface
# ---------------------------------------------------------------------------------
class AttrLengthCorruptionCondition(AccountCorruptionConditionInterface):
    def isCorrupted(self, account : Account) -> bool:
        return isEven(account.get_attr_len())

class AttrNamingCorruptionCondition(AccountCorruptionConditionInterface):
    def isCorrupted(self, account : Account) -> bool:
        return any([key.startswith('b') for key in account.__dict__.keys()])
    
class MandatoryAttrCorruptionCondition(AccountCorruptionConditionInterface):
    def isCorrupted(self, account : Account) -> bool:
        if not self.hasAddressInfo(account):
            return True
        result = [
            self.isZipCorrupted(account),
            self.isAddrCorrupted(account),
        ]
        return all(i == True for i in result)
        
    def hasAddressInfo(self, account : Account) -> bool:
        return hasattr(account, 'zip') or hasattr(account, 'addr')

    def isZipCorrupted(self, account : Account) -> bool:
        for key, value in account.__dict__.items():
            if key.startswith('zip') and type(value) is str:
                return False
        return True
    
    def isAddrCorrupted(self, account : Account) -> bool:
        for key, value in account.__dict__.items():
            if key.startswith('addr') and type(value) is str:
                return False
        return True

class AttrTypeCorruptionCondition(AccountCorruptionConditionInterface):
    def isCorrupted(self, account : Account) -> bool:
        results = [
            self.isValueCorrupted(account),
            self.isNameCorrupted(account),
            self.isIdCorrupted(account)
        ]
        return any(i == True for i in results)
    
    def isValueCorrupted(self, account : Account) -> bool:
        return not hasattr(account, 'value') or (type(account.value) is not int and type(account.value) is not float)
    
    def isNameCorrupted(self, account : Account) -> bool:
        return not hasattr(account, 'name') or type(account.name) is not str
    
    def isIdCorrupted(self, account : Account) -> bool:
        return not hasattr(account, 'id') or type(account.id) is not int
# * classes for Corruption Check End ----------------------------------------------

# * class AccountCorruptionConditionInterface(abstract)
# ---------------------------------------------------------------------------------
class AccountCorruptionFixerInterface(ABC):
    @abstractmethod
    def fix(self, account : Account) -> bool:
        pass
# * class AccountCorruptionCondition End ------------------------------------------

# * classes for fix Corruption : AccountCorruptionConditionInterface
# ---------------------------------------------------------------------------------
class AttrLengthFixer(AccountCorruptionFixerInterface, AttrLengthCorruptionCondition):
    def fix(self, account : Account) -> bool:
        if self.isCorrupted(account):
            account.__dict__['tmp'] = 0
            return True
        return False

class AttrNamingFixer(AccountCorruptionFixerInterface, AttrNamingCorruptionCondition):
    def fix(self, account : Account) -> bool:
        if self.isCorrupted(account):
            new_key = []
            old_key = []
            for key in account.__dict__.keys():
                if key.startswith('b'):
                    old_key.append(key)
                    new_key.append(key[1:])
            for old_key, new_key in zip(old_key, new_key):
                if old_key.find("zip") != -1:
                    new_key = "zip"
                elif old_key.find("addr") != -1:
                    new_key = "addr"
                account.__dict__[new_key] = account.__dict__.pop(old_key)
            return True
        return False
    
class MandatoryAttrFixer(AccountCorruptionFixerInterface, MandatoryAttrCorruptionCondition):
    def fix(self, account : Account) -> bool:
        if self.isCorrupted(account):
            account.__dict__['addr'] = "Unknown"
            account.__dict__['zip'] = "Unknown"
            return True
        return False

class AttrTypeFixer(AccountCorruptionFixerInterface, AttrTypeCorruptionCondition):
    def fix(self, account : Account) -> bool:
        if self.isCorrupted(account):
            if self.isValueCorrupted(account):
                account.__dict__['value'] = 0
            if self.isNameCorrupted(account):
                account.__dict__['name'] = "Unknown"
            if self.isIdCorrupted(account):
                account.__dict__['name'] = Account.ID_COUNT
                Account.ID_COUNT += 1
            return True
        return False
# * classes for fix Corruption End ------------------------------------------------

# * classes for AccountCorruptionCondition End ====================================


# * class AccountCorruptionInspector
# ---------------------------------------------------------------------------------
class AccountCorruptionInspector():
    conditions = [
        AttrLengthCorruptionCondition(),
        AttrNamingCorruptionCondition(),
        AttrTypeCorruptionCondition(),
        MandatoryAttrCorruptionCondition(),
    ]

    def isCorrupted(self, account : Account) -> bool:
        return any([condition.isCorrupted(account) for condition in self.conditions])

# * class AccountCorruptionInspector End ------------------------------------------


# * class AccountFixer
# ---------------------------------------------------------------------------------
class AccountFixer():
    conditions = [
        AttrLengthFixer(),
        AttrNamingFixer(),
        MandatoryAttrFixer(),
        AttrTypeFixer()
    ]

    def fix(self, account : Account) -> bool:
        return any([condition.fix(account) for condition in self.conditions])
# * class AccountFixer End --------------------------------------------------------


# * class Bank
# ---------------------------------------------------------------------------------
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = AccountStorage()
        self.inspector = AccountCorruptionInspector()
        self.account_fixer = AccountFixer()

    def add(self, new_account : Account):
        """
            Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code  ...
        if not isinstance(new_account, Account) or self.accounts.find_account(new_account.name) is not None:
            return False
        return self.accounts.create_account(new_account)

    def transfer(self, origin, dest, amount) -> bool:
        """"
            Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        # ... Your code  ...
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, float):
            return False
        origin_account, dest_account = [self.accounts.find_account(origin), self.accounts.find_account(dest)]
        if None in [origin_account, dest_account]:
            return False
        is_origin_corrupted = self.inspector.isCorrupted(origin_account)
        is_dest_corrupted = self.inspector.isCorrupted(dest_account)
        if True in [is_origin_corrupted, is_dest_corrupted] or \
            origin_account.isBalanced(amount) == False:
            return False
        origin_account.withdraw(amount)
        dest_account.transfer(amount)
        return True
    
    def find_account(self, name : str) -> Account:
        """
            find account associated to name
            @name:   str(name) of the account
            @return  Account() if found, None if not found
        """
        # ... Your code  ...
        if not isinstance(name, str):
            return None
        return self.accounts.find_account(name)


    def fix_account(self, name : str) -> bool:
        """
            fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        # ... Your code  ...
        if not isinstance(name, str):
            return False
        found = self.accounts.find_account(name)
        if found is None:
            return False
        self.account_fixer.fix(found)
        return True
# * class Bank End ----------------------------------------------------------------


# * class AccountStorage
# ---------------------------------------------------------------------------------
class AccountStorage():
    def __init__(self):
        self.accounts = []

    def create_account(self, account : Account) -> bool:
        self.accounts.append(account)
        return True
    
    def find_account(self, name : str) -> Account:
        for account in self.accounts:
            if account.name == name:
                return account
        return None
    
    def remove_account(self, name : str) -> bool:
        for account in self.accounts:
            if account.name == name:
                self.accounts.remove(account)
                return True
        return False
    
    def size(self) -> int:
        return len(self.accounts)
# * class AccountStorage End ------------------------------------------------------