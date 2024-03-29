import unittest
from the_bank import *
import copy
import random   

class PositiveAccountStorage():
    def __init__(self):
        self.lst = []
        
        self.lst.append(Account(
            'William John',
            value=6460.0,
            addr='100-064, 1st street, New York, NY, USA',
            ref='58ba2b9954cd278eda8a84147ca73c87',
        ))

        self.lst.append(Account(
            'John William',
            value=1000.0,
            addr='100-32, 2nd street, New York, NY, USA',
            ref='1044618427ff2782f0bbece0abd05f31',
        ))

        self.lst.append(Account(
            'Jane Smith',
            value=1000.0,
            addr='100-32, 2nd street, New York, NY, USA',
            ref='1044618427ff2782f0bbece0abd05f31',
            joined='2019-01-01',
            zip='911-745',
        ))

    def get(self):
        return self.lst
    
    def print(self):
        for i in self.lst:
            print(i.__dict__)
            print(f"{i} - attr_len : {len(i.__dict__)}")
        print(len(self.lst))
    
class NegativeAccountStorage():
    def __init__(self):
        self.lst = []

        self.lst.append(Account(
            'William John',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            joined='2019-01-01',
            tag='no zip',
        ))

        value_negative = Account(
            'Jane Smith',
            value=1000.0,
            addr='100-32, 2nd street, New York, NY, USA',
            ref='1044618427ff2782f0bbece0abd05f31',
            joined='2019-01-01',
            tag='value is str'
        )
        value_negative.value = '1000.0'
        self.lst.append(value_negative)

        name_negative = Account(
            'Jane Smith',
            value=1000.0,
            addr='100-32, 2nd street, New York, NY, USA',
            ref='1044618427ff2782f0bbece0abd05f31',
            joined='2019-01-01',
            tag='name is not str'
        )
        name_negative.name = 1323231
        self.lst.append(name_negative)

        self.lst.append(Account(
            'John William',
            value=1000.0,
            addr='100-32, 2nd street, New York, NY, USA',
            b_zip='911-745',
            tag='attr starts with b',
        ))

        self.lst.append(Account(
            'Jane Smith',
            value=1000.0,
            addr='100-32, 2nd street, New York, NY, USA',
            ref='1044618427ff2782f0bbece0abd05f31',
            zip='911-745',
            temp='temp',
            tag='len is even',
        ))

    def get(self):
        return self.lst
    
    def print(self):
        for i in self.lst:
            print(i.__dict__)
            print(f"{i} - attr_len : {len(i.__dict__)}")
        print(len(self.lst))

class test_utils(unittest.TestCase):
    def test_isEven(self):
        self.assertTrue(isEven(2))
        self.assertFalse(isEven(3))
        self.assertTrue(isEven(0))
        self.assertFalse(isEven(-1))

    def test_isFloatDigit(self):
        self.assertTrue(isFloatDigit('1'))
        self.assertTrue(isFloatDigit('1.'))
        self.assertTrue(isFloatDigit('1.0'))
        self.assertTrue(isFloatDigit('1.0909988'))
        self.assertTrue(isFloatDigit('1.1'))
        self.assertFalse(isFloatDigit('1.1.1'))
        self.assertFalse(isFloatDigit('a'))
        self.assertFalse(isFloatDigit('1a'))
        self.assertFalse(isFloatDigit('a1'))
        self.assertFalse(isFloatDigit('1.1a'))

class test_Account(unittest.TestCase, PositiveAccountStorage, NegativeAccountStorage):
    positive_accounts = PositiveAccountStorage().get()
    negative_accounts = NegativeAccountStorage().get()
    checker = AccountCorruptionInspector()
    fixer = AccountFixer()

    def test_positive_accounts(self):
        for account in self.positive_accounts:
            self.assertFalse(self.checker.isCorrupted(account))

    def test_fix_positive_accounts(self):
        for account in self.positive_accounts:
            self.assertFalse(self.checker.isCorrupted(account))
            self.fixer.fix(account)
            self.assertFalse(self.checker.isCorrupted(account))

    def test_negative_accounts(self):
        negative_accounts = copy.deepcopy(self.negative_accounts)
        for account in negative_accounts:
            self.assertTrue(self.checker.isCorrupted(account))

    def test_fix_negative_accounts(self):
        negative_accounts = copy.deepcopy(self.negative_accounts)
        for account in negative_accounts:
            self.assertTrue(self.checker.isCorrupted(account))
            self.fixer.fix(account)
            self.assertFalse(self.checker.isCorrupted(account))

    def test_transfer(self):
        positive_accounts = copy.deepcopy(self.positive_accounts)
        for account in positive_accounts:
            old_value = account.value
            account.transfer(1000.0)
            self.assertEqual(account.value, old_value + 1000.0)

    def test_transfer_negative(self):
        positive_accounts = copy.deepcopy(self.positive_accounts)
        for account in positive_accounts:
            old_value = account.value
            result = account.transfer(-1000.0)
            self.assertEqual(account.value, old_value)
            self.assertFalse(result)
    
    def test_randomly_withdraw(self):
        positive_accounts = copy.deepcopy(self.positive_accounts)
        batch_size = 10000
        for _ in range(batch_size):
            for account in positive_accounts:
                base = 2000
                old_value = account.value
                amount = random.randint(0, base)
                expected = True if old_value - amount >= 0 else False
                self.assertEqual(account.withdraw(amount), expected)
                if expected:
                    self.assertEqual(account.value, old_value - amount)

class test_AccountStorage(unittest.TestCase, PositiveAccountStorage):
    positive_accounts = PositiveAccountStorage().get()

    def test_AccountStorage(self):
        storage = AccountStorage()    
        for account in self.positive_accounts:
            storage.create_account(account)
        self.assertEqual(storage.size(), len(self.positive_accounts))

        for account in self.positive_accounts:
            self.assertEqual(storage.find_account(account.name), account)

        for account in self.positive_accounts:
            storage.remove_account(account.name)
            self.assertEqual(storage.find_account(account.name), None)
        self.assertEqual(storage.size(), 0)

class test_subject_cases(unittest.TestCase):
    def test_case_01(self):
        bank = Bank()
        bank.add(Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        ))
        bank.add(Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None
        ))

        result = bank.transfer('William John', 'Smith Jane', 1000.0)
        self.assertFalse(result)

    def test_case_02(self):
        bank = Bank()
        account_00 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        )
        account_01 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None
        )

        bank.add(account_00)
        bank.add(account_01)

        result = bank.transfer('William John', 'Smith Jane', 1000.0)
        self.assertFalse(result)

        bank.fix_account('William John')
        bank.fix_account('Smith Jane')

        result = bank.transfer('William John', 'Smith Jane', 1000.0)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()