class Shape:
    def __init__(self, obj='Shape'):
        print('Конструктор объекта: ', obj)
    def show(self,obj='Shape'):
        print('Метод объекта ', obj)

class Point(Shape):
    def __init__(self, obj='Point'):
        self.x = 0
        self.y = 0
        Shape.__init__(self, obj)
    def show(self, obj = 'Point'):
        Shape.show(self, obj)    
    
class Circle(Point):
    def __init__(self, obj='Circle'):
        self.r = 1
        Shape.__init__(self, obj)
    def show(self, obj = 'Circle'):
        Shape.show(self, obj)
        
class Square(Shape):
    def __init__(self, obj='Square'):
        a = 4
        Shape.__init__(self, obj)
    def show(self,obj='Skuare'):
        Shape.show(self, obj)
