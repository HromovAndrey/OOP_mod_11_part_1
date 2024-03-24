#Завдання 5
#Створіть клас BankAccount з атрибутами balance
#та owner, а також методами deposit та withdraw для
#здійснення операцій з балансом. Реалізуйте перевірку
#на те, що баланс не може стати від'ємним.
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнення на {amount} грн успішно здійснено.")
        else:
            print("Помилка: Сума поповнення повинна бути більше нуля.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Зняття {amount} грн успішно здійснено.")
            else:
                print("Помилка: Недостатньо коштів на рахунку.")
        else:
            print("Помилка: Сума зняття повинна бути більше нуля.")

account = BankAccount("John Doe", 1000)
print(f"Баланс рахунку: {account.balance} грн")

account.deposit(500)
print(f"Після поповнення баланс рахунку: {account.balance} грн")

account.withdraw(200)
print(f"Після зняття баланс рахунку: {account.balance} грн")

account.withdraw(2000)
print(f"Після спроби зняття недостатньої суми баланс рахунку: {account.balance} грн")