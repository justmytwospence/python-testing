from contextlib import contextmanager


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


@contextmanager
def managed_file(name):
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()


if __name__ == "__main__":
    mf = ManagedFile("hello.txt")
    with mf as f:
        f.write("Hellowurld")

    with managed_file("hello.txt") as f:
        f.write("Hellowurld")