class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f'Width: {self.width} | Height: {self.height}'

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    # Setters here are violating the Liskov substitution principle.
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    # Setters here are violating the Liskov substitution principle.
    def height(self, value):
        self._width = self._height = value

    # In order to comply with the LSP, remove the getter and setter from the inhereting class - Square

def use_shape(rect):
    w = rect.width
    rect.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, but got {rect.area}')


rect = Rectangle(2,3)
use_shape(rect=rect)

sq = Square(5)
use_shape(sq)