"""lUIS ANGEL VELAZZQUEZ JIMENEZ"""
"""GRUPO:GITI-9072-e"""
"""NO:1215100974"""

class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class DrawingAPITwo(object):
    """Implementation-specific abstraction: class two"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class Circle(object):
    """Implementation-independient abtraction: for example, there could be a rectangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attribute"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-especific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Impementation-independient"""
        self._radius *= percent

circle1 = Circle(1, 2, 3, DrawingAPIOne())

circle1.draw()

circle2 = Circle(2, 3, 4, DrawingAPITwo())

circle2.draw()
