import pytest

from palindrome import is_palindrome, is_palindrome_recursive


class TestPalindrome:

    @pytest.fixture
    def tacocat(self):
        return 'tacocat'

    @pytest.fixture
    def not_palindrome(self):
        return 'not_palindrome'

    def test_is_palindrome(self, tacocat, not_palindrome):
        assert is_palindrome(tacocat)
        assert not is_palindrome(not_palindrome)

    def test_is_palindrome_recursive(self, tacocat, not_palindrome):
        assert is_palindrome_recursive(tacocat)
        assert not is_palindrome_recursive(not_palindrome)
