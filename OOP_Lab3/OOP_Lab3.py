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


class Node:
    def __init__(self,obj=None, next = None):
        self.obj = obj
        self.next = next

    
class Storage:
    def __init__(self):
        self.first = None
    def add(self,new_obj,position):
        if self.first == None:
            self.first = Node(new_obj,None)
            return
        if position == 0:
            self.first = Node(new_obj,self.first)
            return
        current = self.first
        count = 0
        while current!=None:
            count+=1
            if count == position:
                current.next = Node(new_obj,current.next)
                return
            current = current.next
         
    def delete(self,position):
        if self.first == None:
            return
        current = self.first
        if position == 0:
            self.first = self.first.next
            return
        count = 0
        while current != None:
            if count == position:
                old.next=current.next
                return
            old = current
            current = current.next
            count += 1
    def length(self):
        length = 0
        if self.first == None:
            return 0
        current = self.first
        while current.next != None:
            current = current.next
            length += 1
        return length + 1 