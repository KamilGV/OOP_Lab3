import random
import time

class Shape:
    def __init__(self, obj='Shape'):
        print('Конструктор', obj)
    def show(self,obj='Shape'):
        print('Метод', obj)
    def __del__(self, obj='Shape'):
        print('Деструктор', obj)
        
class Point(Shape):
    def __init__(self, obj='Point'):
        self.x = 0
        self.y = 0
        Shape.__init__(self, obj)
    def show(self, obj = 'Point'):
        Shape.show(self, obj)
    def __del__(self, obj='Point'):
        Shape.__del__(self,obj)
    
class Circle(Point):
    def __init__(self, obj='Circle'):
        self.r = 1
        Shape.__init__(self, obj)
    def show(self, obj = 'Circle'):
        Shape.show(self, obj)
    def __del__(self, obj='Circle'):
        Shape.__del__(self,obj)
        
class Square(Shape):
    def __init__(self, obj='Square'):
        self.a = 4
        Shape.__init__(self, obj)
    def show(self,obj='Square'):
        Shape.show(self, obj)
    def __del__(self, obj='Square'):
        Shape.__del__(self,obj)



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
    def get_object(self,n):
        count = 0
        current = self.first
        while 1:
            if count == n:
                return current.obj
            current = current.next
            count+=1
            
            
if __name__ == '__main__':
    start = time.time()
    n = 100
    s = Storage()
    for i in range(3):
        s.add(Point(),0)
        s.add(Circle(),0)
        s.add(Square(),0)

    for i in range(n):
        n = random.randrange(0,s.length())
        m = random.choice([3,6,9,12,5,8,7,10,13])
        obje = random.choice([Shape,Point,Circle,Square])
        if m%3==2:
            s.delete(n)
        elif m%3==0:
            obje = random.choice([Shape,Point,Circle,Square])
            s.add(obje(),n)
        else:
            s.get_object(n).show()
    print('Время работы: %.4f секунды.' % (time.time()-start))
