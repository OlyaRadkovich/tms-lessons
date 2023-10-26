import os.path
import random
import json


def random_digits(count: int) -> str:
    random_num = ''
    for _ in range(count):
        random_num += str(random.randint(1, 9))
    return random_num


class BankAccount:
    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None):
        self.card_holder: str = card_holder.upper()
        self.money: float = money
        self.account_number: str = random_digits(20) if account_number is None \
            else account_number
        self.card_number: str = random_digits(16) if card_number is None else card_number


def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
    return {
        'card_holder': bank_account.card_holder,
        'card_number': bank_account.card_number,
        'account_number': bank_account.account_number,
        'money': bank_account.money
    }


def save_accounts(bank_accounts: dict[str, BankAccount], file_name: str):
    data = {number: convert_bank_account_to_dict(account)
            for number, account in bank_accounts.items()}
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


def load_accounts(file_name) -> dict[str, BankAccount]:
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        return {number: BankAccount(**data) for number, data in json.load(file).items()}


class Bank:
    def __init__(self, bank_accounts=None):
        self.bank_accounts: dict[str, BankAccount] = bank_accounts or {}

    def open_account(self, card_holder) -> BankAccount:
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number: str, money: float):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        from_account = self.bank_accounts[from_account_number]
        to_account = self.bank_accounts[to_account_number]
        from_account.money -= money
        to_account.money += money

    def external_transfer(self, from_account_number, external_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account.money -= money
        print(f'Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {external_number}')


class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts: dict[str, BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж ')
            action = int(input())
            if action == 0:
                print('До свидания!')
                save_accounts(self.bank.bank_accounts, self.data_file_name)
                break
            elif action == 1:
                card_holder = input(f'Введите имя и фамилию держателя карты(на английском): ')
                account = self.bank.open_account(card_holder)
                print(f'Счёт {account.account_number} создан')
            elif action == 2:
                self.show_accounts()
            elif action == 3:
                account = input(f'Введите номер счёта ')
                money = float(input(f'Введите сумму пополнения '))
                self.bank.add_money(account, money)
            elif action == 4:
                from_account_number = input(f'Введите номер счёта отправителя ')
                to_account_number = input(f'Введите номер счёта получателя ')
                money = float(input(f'Сумма перевода: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)
            elif action == 5:
                from_account_number = input(f'Введите номер счёта отправителя ')
                external_account = input(f'Введите номер счёта получателя ')
                money = float(input(f'Сумма перевода: '))
                self.bank.external_transfer(from_account_number, external_account, money)
            else:
                print('Вы ввели неподдерживаемую команду')

    def show_accounts(self):
        print('Открытые счета:')
        for account_number, account in self.bank.bank_accounts.items():
            print(f'Держатель карты: {account.card_holder}')
            print(f'Номер карты: {account.card_number}')
            print(f'Номер счета: {account_number}')
            print(f'Остаток на счете: {account.money} $')


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
