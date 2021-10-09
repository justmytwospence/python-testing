import types

import pytest
from my_zip import my_zip


class TestMyZip:

    def test_lists(self):
        z = my_zip([1, 2, 3], [4, 5, 6])
        assert next(z) == (1, 4)
        assert list(z) == [(2, 5), (3, 6)]

    def test_three_lists(self):
        z = my_zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
        assert next(z) == (1, 4, 7)
        assert list(z) == [(2, 5, 8), (3, 6, 9)]

    def test_empty(self):
        z = my_zip([])
        assert isinstance(z, types.GeneratorType)
        with pytest.raises(StopIteration):
            next(z)
