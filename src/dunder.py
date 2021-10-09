from functools import total_ordering


@total_ordering
class Account:

    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        return f'{self.owner} owns {self.amount}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.owner}", {self.amount})'

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Please use an integer for amount")
        else:
            self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return list(reversed(self._transactions))

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = f'{self.owner}&{other.owner}'
        amount = self.amount + other.amount
        account = Account(owner, amount)
        for transaction in list(self) + list(other):
            account.add_transaction(transaction)
        return account

    def __enter__(self):
        print('ENTER WITH: making backup of transactions for rollback')
        self._copy_transactions = self._transactions
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print('Rolling back to previous transactions')
            print(f'Transaction resulted in {exc_type.__name__}, {exc_val}')
        else:
            print('Transaction OK')
