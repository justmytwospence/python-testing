import importlib


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def whatami(self):
        return 'Rectangle'


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length, width=length, **kwargs)

    def whatami(self):
        return 'Square'


class Cube(Square):

    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def whatami(self):
        return 'Cube'

    def familytree(self):
        return self.whatami()  # + ' child of ' + super().whatami()


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def area(self):
        return 0.5 * self.base * self.height

    def whatami(self):
        return 'Triangle'


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['length'] = base
        super().__init__(base=base, **kwargs)

    def whatami(self):
        return 'RightPyramid'
