import pytest

from bloomfilter import BloomFilter


class TestBloomFilter:

    @pytest.fixture
    def bf(self):
        return BloomFilter(['foo', 'bar'])

    def test_constructor(self, bf):
        assert isinstance(bf, BloomFilter)

    def test_add(self, bf):
        bf.add('baz')
        assert 'baz' in bf

    def test_in(self, bf):
        assert 'foo' in bf
        assert 'wiz' not in bf

    def test_delete(self, bf):
        bf.delete('foo')
        assert 'foo' not in bf
