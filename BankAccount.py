import threading
import time

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited: {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn: {amount}, Balance: {self.balance}")
            else:
                print("Insufficient funds")

def transaction(account, amount, type):
    if type == "deposit":
        account.deposit(amount)
    else:
        account.withdraw(amount)

def main():
    account = BankAccount(1000)

    threads = []
    for i in range(10):
        thread = threading.Thread(target=transaction, args=(account, 100, "deposit"))
        thread.start()
        threads.append(thread)

    for i in range(10):
        thread = threading.Thread(target=transaction, args=(account, 50, "withdraw"))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
