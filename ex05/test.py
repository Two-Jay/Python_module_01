import unittest
from the_bank import *

class test_account(unittest.TestCase):
    def test_declare(self):
        a = Account("test", value=100, zip=12345, addr="test")
        self.assertIsInstance(a, Account)
        self.assertEqual(a.name, "test")
        self.assertEqual(a.value, 100)
        self.assertEqual(a.zip, 12345)
    
    def test_transfer(self):
        a = Account("test", value=100, zip=12345, addr="test")
        self.assertIsInstance(a, Account)
        a.transfer(50)
        self.assertEqual(a.value, 150)

    def test_widthrow(self):
        a = Account("test", value=100, zip=12345, addr="test")
        self.assertIsInstance(a, Account)
        a.widthrow(50)
        self.assertEqual(a.value, 50)

    def test_isEnough(self):
        a = Account("test", value=100, zip=12345, addr="test")
        self.assertIsInstance(a, Account)
        self.assertEqual(a.isEnough(50), True)
        self.assertEqual(a.isEnough(150), False)

    def test_subject_account(self):
        ac1 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        self.assertIsInstance(ac1, Account)
        self.assertEqual(len(ac1.__dict__), 5)
        self.assertEqual(ac1.name, 'Smith Jane')
        self.assertEqual(ac1.value, 1000.0)
        self.assertEqual(ac1.zip, '911-745')

        self.assertRaises(AttributeError, lambda: ac1.addr)

        ac2 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation'
        )

        self.assertIsInstance(ac2, Account)
        self.assertEqual(len(ac2.__dict__), 7)
        self.assertEqual(ac2.name, 'William John')
        self.assertEqual(ac2.value, 6460.0)
        self.assertEqual(ac2.zip, '100-064')
        self.assertEqual(ac2.ref, '58ba2b9954cd278eda8a84147ca73c87')
        self.assertEqual(ac2.other, 'This is the vice president of the corporation')

        self.assertRaises(AttributeError, lambda: ac2.addr)
        self.assertRaises(AttributeError, lambda: ac2.bref)

        test_value = 545.0
        self.assertEqual(ac1.widthrow(test_value), True)
        self.assertEqual(ac2.transfer(test_value), True)

        self.assertEqual(ac1.value, 1000.0 - test_value)
        self.assertEqual(ac2.value, 6460.0 + test_value)

    def test_Account_negative_00(self):
        a = Account("test", value=100, zip=12345, addr="test")
        self.assertIsInstance(a, Account)
        a.widthrow(150)
        self.assertNotEqual(a.value, 50)

class test_Account_storage(unittest.TestCase):
    def test_Account_storage_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac_storage = Account_storage()
        
        self.assertIsInstance(ac, Account)
        self.assertIsInstance(ac_storage, Account_storage)
        self.assertEqual(ac_storage.create(ac), True)

    def test_Account_storage_01(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac_storage = Account_storage()
        
        ac_storage.create(ac)
        found = ac_storage.find_by_name(ac.name)
        self.assertEqual(found, ac)

        test_value = 100.0
        original_value = ac.value
        found.widthrow(test_value)
        self.assertEqual(found.value, original_value - test_value)

    def test_Account_storage_02(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac_storage = Account_storage()
        
        ac_storage.create(ac)
        found = ac_storage.find_by_name(ac.name)
        self.assertEqual(found, ac)

        test_value = 100.0
        original_value = ac.value
        found.transfer(test_value)
        self.assertEqual(found.value, original_value + test_value)

    def test_Account_storage_03(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
        ac_storage = Account_storage()
        ac_storage.create(ac)

        found = ac_storage.find_by_name(ac.name)
        self.assertEqual(found, ac)
        ac_storage.remove(ac)

        found = ac_storage.find_by_name(ac.name)
        self.assertEqual(found, None)


class test_Right_account_inspector(unittest.TestCase):
    def test_rightcheck_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
        
        self.assertIsInstance(ac, Account)
        self.assertEqual(Right_account_inspector.inspect(ac), True)

    def test_rightcheck_01(self):            
        ac = int(1)
        
        self.assertIsInstance(ac, int)
        self.assertEqual(Right_account_inspector.inspect(ac), False)

    def test_rightcheck_02(self):
        ac = str("test")

        self.assertIsInstance(ac, str)
        self.assertEqual(Right_account_inspector.inspect(ac), False)

    def test_rightcheck_03(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
        
        self.assertIsInstance(ac, Account)
        self.assertEqual(Right_account_inspector.inspect(str(ac)), False)

    def test_rightcheck_04(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
        
        self.assertIsInstance(ac, Account)
        self.assertEqual(Right_account_inspector.inspect(repr(ac)), False)

    def test_rightcheck_05(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
        
        self.assertIsInstance(ac, Account)
        self.assertEqual(Right_account_inspector.inspect(ac.name), False)

class test_Balance_checker(unittest.TestCase):
    def test_balance_check_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        test_value = 300.0

        self.assertIsInstance(ac, Account)
        self.assertEqual(Balance_inspector.inspect(ac, test_value), True)

    def test_balance_check_01(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        test_value = 1500.0

        self.assertIsInstance(ac, Account)
        self.assertEqual(Balance_inspector.inspect(ac, test_value), False)
        
    def test_balance_check_02(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        test_value = ac.value

        self.assertIsInstance(ac, Account)
        self.assertEqual(Balance_inspector.inspect(ac, test_value), True)

    def test_balance_check_03(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        test_value = 300

        self.assertIsInstance(ac, Account)
        self.assertEqual(Balance_inspector.inspect(ac, test_value), True)

    def test_balance_check_04(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        test_value = 1500

        self.assertIsInstance(ac, Account)
        self.assertEqual(Balance_inspector.inspect(ac, test_value), False)
        
    def test_balance_check_05(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        test_value = "hello"

        self.assertIsInstance(ac, Account)
        self.assertRaises(TypeError, lambda: Balance_inspector.inspect(ac, test_value))

class test_Corrupt_account_inspector(unittest.TestCase):
    def test_corrupt_check_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_type(ac), True)
        
    def test_corrupt_check_01(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac.value = "1000.0"

        self.assertRaises(AccountCorruptionException, lambda: Corrupt_account_inspector.check_attr_type(ac))


        
    

if __name__ == '__main__':
    unittest.main()