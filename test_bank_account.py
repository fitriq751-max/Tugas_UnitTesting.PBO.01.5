import unittest
# Mengimpor kelas BankAccount dari file bank_account.py
from bank_account import BankAccount 

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        "Menyiapkan objek BankAccount sebelum setiap pengujian dijalankan."
        self.account = BankAccount("Fitri Khairani", 1000)

    def test_initialization(self):
        "Menguji apakah inisialisasi saldo dan pemilik sudah benar."
        self.assertEqual(self.account.owner, "Fitri Khairani")
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_success(self):
        "Menguji penambahan saldo yang valid."
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_error(self):
        "Menguji bahwa deposit angka nol atau negatif akan memicu ValueError."
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw_success(self):
        "Menguji penarikan saldo yang valid."
        self.account.withdraw(400)
        self.assertEqual(self.account.get_balance(), 600)

    def test_withdraw_insufficient_funds(self):
        "Menguji penarikan yang melebihi saldo (harus memicu ValueError)."
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_withdraw_invalid_amount(self):
        "Menguji penarikan dengan angka nol atau negatif."
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

if __name__ == '__main__':
    unittest.main()