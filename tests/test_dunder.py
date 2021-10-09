import pytest
from dunder import Account


class TestAccount:

    @pytest.fixture
    def empty_account(self):
        return Account("Spencer", 37)

    @pytest.fixture
    def loaded_account(self):
        account = Account("Spencer", 37)
        account.add_transaction(1)
        account.add_transaction(-2)
        account.add_transaction(3)
        return account

    @pytest.fixture
    def huge_account(self):
        return Account("Moneybags", float('inf'))

    def test_constructor(self, empty_account):
        assert isinstance(empty_account, Account)
        assert empty_account.owner == "Spencer"
        assert empty_account.amount == 37

    def test_str(self, empty_account):
        assert str(empty_account) == 'Spencer owns 37'

    def test_repr(self, empty_account):
        assert repr(empty_account) == 'Account("Spencer", 37)'

    def test_add_transaction(self, empty_account):
        empty_account.add_transaction(17)
        assert empty_account._transactions == [17]
        with pytest.raises(ValueError):
            empty_account.add_transaction('17')

    def test_balance(self, loaded_account):
        assert loaded_account.balance == 39

    def test_len(self, loaded_account):
        assert len(loaded_account) == 3

    def test_getitem(self, loaded_account):
        assert loaded_account[2] == 3
        with pytest.raises(IndexError):
            loaded_account[3]

    def test_reversed(self, loaded_account):
        assert reversed(loaded_account) == [3, -2, 1]

    def test_comparisons(self, empty_account, huge_account):
        assert empty_account < huge_account
        assert huge_account > empty_account
        assert huge_account != empty_account
        assert empty_account == empty_account
        assert huge_account == huge_account

    def test_add(self, loaded_account):
        merged = loaded_account + loaded_account
        assert merged.owner == 'Spencer&Spencer'
        assert merged.balance == 39 + 39
        assert merged._transactions == [1, -2, 3, 1, -2, 3]
