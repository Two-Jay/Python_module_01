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
        test_func = lambda: Balance_inspector.inspect(ac, test_value)

        self.assertIsInstance(ac, Account)
        self.assertRaises(TypeError, test_func)

class test_Corrupt_account_inspector_method(unittest.TestCase):
    def test_corrupt_check_attr_type_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_type(ac), True)
        
    def test_corrupt_check_attr_type_01(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac.value = "1000.0"
        test_func = lambda: Corrupt_account_inspector.check_attr_type(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_type_02(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac.name = 1
        test_func = lambda: Corrupt_account_inspector.check_attr_type(ac)
        self.assertRaises(AccountCorruptionException, test_func)
    
    def test_corrupt_check_attr_type_03(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac.id = "1"
        test_func = lambda: Corrupt_account_inspector.check_attr_type(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_type_04(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        ac.zip = 911745
        self.assertEqual(Corrupt_account_inspector.check_attr_type(ac), True)

    def test_corrupt_check_attr_len_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_len(ac), True)

    def test_corrupt_check_attr_len_01(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
        )

        test_func = lambda: Corrupt_account_inspector.check_attr_len(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_len_02(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_len(ac), True)

    def test_corrupt_check_attr_len_03(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
        )

        del ac.value
        test_func = lambda: Corrupt_account_inspector.check_attr_len(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_len_04(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
        )

        del ac.id
        del ac.name

        test_func = lambda: Corrupt_account_inspector.check_attr_len(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_len_04(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
        )

        del ac.id
        del ac.name
        del ac.value

        test_func = lambda: Corrupt_account_inspector.check_attr_len(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_name_00(self):
        ac = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_name(ac), True)

    def test_corrupt_check_attr_name_01(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            address='123 Main St'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_name(ac), True)

    def test_corrupt_check_attr_name_02(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            address='123 Main St'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_name(ac), True)

    def test_corrupt_check_attr_name_03(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_name(ac), True)

    def test_corrupt_check_attr_name_04(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
            address='123 Main St'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_name(ac), True)

    def test_corrupt_check_attr_name_05(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
        )

        test_func = lambda: Corrupt_account_inspector.check_attr_name(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_name_06(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            address='123 Main St'
        )

        del ac.address
        test_func = lambda: Corrupt_account_inspector.check_attr_name(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_name_07(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        del ac.zip_code
        test_func = lambda: Corrupt_account_inspector.check_attr_name(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_name_08(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip='911-745',
        )

        del ac.zip
        test_func = lambda: Corrupt_account_inspector.check_attr_name(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_name_09(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            addr='123 Main St',
        )

        del ac.addr
        test_func = lambda: Corrupt_account_inspector.check_attr_name(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_name_10(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip='911-745',
        )

        ac.__dict__['noname'] = ac.__dict__.pop('zip')
        test_func = lambda: Corrupt_account_inspector.check_attr_name(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_mandatory_attr_00(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

    def test_corrupt_check_mandatory_attr_01(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            address='123 Main St'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

    def test_corrupt_check_mandatory_attr_02(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

        del ac.value

        test_func = lambda: Corrupt_account_inspector.check_mandatory_attr(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_mandatory_attr_03(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

        del ac.name

        test_func = lambda: Corrupt_account_inspector.check_mandatory_attr(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_mandatory_attr_03(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

        del ac.id

        test_func = lambda: Corrupt_account_inspector.check_mandatory_attr(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_mandatory_attr_04(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

        ac.__dict__['noname'] = ac.__dict__.pop('value')

        test_func = lambda: Corrupt_account_inspector.check_mandatory_attr(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_mandatory_attr_05(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

        ac.__dict__['noname'] = ac.__dict__.pop('name')

        test_func = lambda: Corrupt_account_inspector.check_mandatory_attr(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_mandatory_attr_06(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_mandatory_attr(ac), True)

        ac.__dict__['noname'] = ac.__dict__.pop('id')

        test_func = lambda: Corrupt_account_inspector.check_mandatory_attr(ac)
        self.assertRaises(AccountCorruptionException, test_func)

    def test_corrupt_check_attr_key_validity(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745'
        )

        self.assertEqual(Corrupt_account_inspector.check_attr_key_validity(ac), True)

    def test_corrupt_check_attr_key_validity_01(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
            baddr='123 Main St'
        )

        test_func = lambda: Corrupt_account_inspector.check_attr_key_validity(ac)
        self.assertRaises(AccountCorruptionException, test_func)

class Test_Corruption_Check(unittest.TestCase):

    def test_corrupt_check_00(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
            addr='123 Main St'
        )
        self.assertEqual(Corrupt_account_inspector.inspect(ac), True)

    def test_corrupt_check_01(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        del ac.zip_code
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_02(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        del ac.value
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_03(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        del ac.name
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_04(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        del ac.id
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_05(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
            b_addr='123 Main St'
        )

        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_06(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        ac.__dict__['noname'] = ac.__dict__.pop('value')
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_07(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        ac.__dict__['noname'] = ac.__dict__.pop('name')
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_08(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        ac.__dict__['noname'] = ac.__dict__.pop('id')
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

    def test_corrupt_check_09(self):
        ac = Account(
            'Smith Jane',
            value=1000.0,
            zip_code='911-745',
        )

        ac.__dict__['noname'] = ac.__dict__.pop('zip_code')
        self.assertEqual(Corrupt_account_inspector.inspect(ac), False)

class test_Bank(unittest.TestCase):

    def test_bank_00(self):
        bank = Bank()


class test_subject_cases(unittest.TestCase):

    def test_00(self):
        bank = Bank()

        ac0 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
        ac1 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation'
        )

        corruption_check_ac00 = Corrupt_account_inspector.inspect(ac0)
        corruption_check_ac01 = Corrupt_account_inspector.inspect(ac1)

        self.assertEqual(corruption_check_ac00, False)
        self.assertEqual(corruption_check_ac01, True)

        self.assertEqual(bank.add(ac0), False)
        self.assertEqual(bank.add(ac1), True)

    
    def test_01(self):
        bank = Bank()

        ac0 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        )
        ac1 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None
        )

        corruption_check_ac00 = Corrupt_account_inspector.inspect(ac0)
        corruption_check_ac01 = Corrupt_account_inspector.inspect(ac1)

        self.assertEqual(corruption_check_ac00, True)
        self.assertEqual(corruption_check_ac01, False)

        self.assertEqual(bank.add(ac0), True)
        self.assertEqual(bank.add(ac1), False)

    def test_02(self):
        bank = Bank()

        ac0 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        ) # len = 5
        ac1 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation'
        ) # len = 7

        corruption_check_ac00 = Corrupt_account_inspector.inspect(ac0)
        corruption_check_ac01 = Corrupt_account_inspector.inspect(ac1)

        self.assertEqual(corruption_check_ac00, False)
        self.assertEqual(corruption_check_ac01, True)

        self.assertEqual(bank.add(ac0), False)
        self.assertEqual(bank.add(ac1), True)

        self.assertEqual(bank.transfer('William John', 'Smith Jane', 1000.0), False)

        self.assertEqual(bank.find_account('William John'), ac1)
        self.assertEqual(bank.find_account('Smith Jane'), None)


    def test_03(self):
        bank = Bank()
        acc_valid_1 = Account('Sherlock Holmes',
                            zip='NW1 6XE',
                            addr='221B Baker street',
                            value=1000.0)
        acc_invalid_2 = Account('James Watson',
                            zip='NW1 6XE',
                            addr='221B Baker street',
                            value=25000.0,
                            info=None)
        acc_valid_2 = Account("Douglass",
                                zip='42',
                                addr='boulevard bessieres',
                                value=42)
        acc_valid_3 = Account("Adam",
                                value=42,
                                zip='0',
                                addr='Somewhere')
        acc_valid_4 = Account("Bender Bending RodrÃ­guez",
                                zip='1',
                                addr='Mexico',
                                value=42)
        acc_valid_5 = Account("Charlotte",
                                zip='2',
                                addr='Somewhere in the Milky Way',
                                value=42)
        acc_valid_6 = Account("Edouard",
                                zip='3',
                                addr='France',
                                value=42)

        self.assertEqual(bank.add(acc_valid_1), True)
        self.assertEqual(bank.add(acc_invalid_2), False)
        self.assertEqual(bank.add(acc_valid_2), True)
        self.assertEqual(bank.add(acc_valid_3), True)
        self.assertEqual(bank.add(acc_valid_4), True)
        self.assertEqual(bank.add(acc_valid_5), True)
        self.assertEqual(bank.add(acc_valid_6), True)

    def test_04(self):
        bank = Bank()

        ac0 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        ) # len = 5
        ac1 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation'
        ) # len = 7

        corruption_check_ac00 = Corrupt_account_inspector.inspect(ac0)
        corruption_check_ac01 = Corrupt_account_inspector.inspect(ac1)

        self.assertEqual(corruption_check_ac00, True)
        self.assertEqual(corruption_check_ac01, True)

        bank.add(ac0)
        bank.add(ac1)

        self.assertEqual(bank.transfer('William John', 'Smith Jane', 1000.0), True)
        self.assertEqual(bank.find_account('William John').value, 5460.0)
        self.assertEqual(bank.find_account('Smith Jane').value, 2000.0)

    def test_05(self):
        bank = Bank()

        ac0 = Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        ) # len = 5
        ac1 = Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation'
        ) # len = 7

        corruption_check_ac00 = Corrupt_account_inspector.inspect(ac0)
        corruption_check_ac01 = Corrupt_account_inspector.inspect(ac1)

        self.assertEqual(corruption_check_ac00, True)
        self.assertEqual(corruption_check_ac01, True)

        bank.add(ac0)
        bank.add(ac1)

        self.assertEqual(bank.find_account('Smith Jane'), ac0)
        self.assertEqual(bank.find_account('William John'), ac1)

        tmp = bank.find_account('William John').__dict__.pop('value')
        corruption_check = Corrupt_account_inspector.inspect(bank.find_account('William John'))

        self.assertEqual(corruption_check, False)

        bank.fix_account('William John')
        target = bank.find_account('William John')
        corruption_check = Corrupt_account_inspector.inspect(target)

        self.assertEqual(corruption_check, True)



if __name__ == '__main__':
    unittest.main()