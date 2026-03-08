import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Menyiapkan objek BankAccount untuk setiap kasus pengujian."""
        # Menggunakan identitas kamu sebagai pemilik akun
        self.account = BankAccount("Fitri Khairani", 1000)

    def test_initialization(self):
        """Menguji apakah inisialisasi atribut private berhasil dilakukan."""
        self.assertEqual(self.account.get_owner(), "Fitri Khairani")
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        """Menguji fungsi penambahan saldo."""
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        """Menguji fungsi penarikan saldo yang valid."""
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_invalid_deposit(self):
        """Menguji apakah error muncul saat deposit jumlah negatif."""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_insufficient_funds(self):
        """Menguji apakah error muncul saat saldo tidak mencukupi."""
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

if __name__ == "__main__":
    unittest.main()
