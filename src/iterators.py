import doctest


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        # return RepeaterIterator(self)
        return self
    
    def __next__(self):
        return self.value


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_repeats:
            self.count += 1
            return self.value
        else:
            raise StopIteration

if __name__ == "__main__":
    doctest.testmod()
    repeater = BoundedRepeater('Hello', 4)
    for x in repeater:
        print(x)
