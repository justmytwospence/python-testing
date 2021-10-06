import doctest
import datetime


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f'A {self.color} car'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'


def main():
    mycar = Car('red', 3214)
    print(mycar)
    today = datetime.date.today()
    print(str(today))
    return mycar


if __name__ == "__main__":
    doctest.testmod()
    main()
