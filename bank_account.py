class BankAccount:
    def __init__(self, owner, balance=0):
        # Menggunakan double underscore agar menjadi private
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        """Menambahkan saldo dengan validasi jumlah positif."""
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            raise ValueError("Jumlah deposit harus lebih dari nol")

    def withdraw(self, amount):
        """Mengurangi saldo dengan pengecekan kecukupan saldo."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            raise ValueError("Saldo tidak mencukupi atau jumlah tidak valid")

    # Metode 'getter' agar Unit Test tetap bisa mengakses nilai secara aman
    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner
