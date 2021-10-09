import doctest

import pyhash


class BloomFilter:
    """Implements a counting Bloom filter"""

    def __init__(self, items=None, size=64):
        self.size = size
        self.bitmap = [0 for _ in range(size)]
        if items is not None:
            for item in items:
                self.add(item)

    def __len__(self):
        return self.size

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.bitmap})'

    def __str__(self) -> str:
        return f'{self.bitmap}'

    def hashes(self, item):
        naive_hash = sum([ord(letter) for letter in item])
        fnv_hash = pyhash.fnv1_32()
        murmur_hash = pyhash.murmur3_32()
        return naive_hash, fnv_hash(item), murmur_hash(item)

    def add(self, item):
        for item_hash in self.hashes(item):
            bitmap_idx = item_hash % self.size
            self.bitmap[bitmap_idx] += 1

    def __contains__(self, item):
        bitmap_idxs = [item_hash % self.size
                       for item_hash in self.hashes(item)]
        if all([self.bitmap[i] for i in bitmap_idxs]):
            return True  # MIGHT be present
        else:
            return False  # DEFINITELY not present

    def delete(self, item):
        bitmap_idxs = [item_hash % self.size
                       for item_hash in self.hashes(item)]
        for i in bitmap_idxs:
            self.bitmap[i] -= 1


if __name__ == "__main__":
    doctest.testmod()
