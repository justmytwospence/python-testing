import math


class MyClass:
    def my_instance_method(self):
        return 'instance method called', self

    @classmethod
    def my_class_method(cls):
        return 'class method called', cls

    @staticmethod
    def my_static_method():
        return 'static method called'


class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'{__class__.__name__}({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'], None)

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham'], None)

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi


if __name__ == "__main__":
    obj = MyClass()
    print(obj.my_instance_method())
    print(obj.my_class_method())
    print(obj.my_static_method())
    print(Pizza(['cheese', 'tomatoes', 'ham', 'mushrooms'], None))
    print(Pizza.margherita())
    print(Pizza.prosciutto())
    print(Pizza(['cheese'], 4.5).area())
