from abc import ABC,abstractmethod
x=int(input("Press 1 for rectangle and press 2 for square"))

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def  area(self):
        return f"the area is {self.a*self.b}"

class Square(Shape):
    def __init__(self, a):
        self.a=a

    def area(self):
        return f"the area is {self.a * self.a}"
if x==1:
    a=int(input("Enter the first side "))
    b=int(input("Enter the second side "))
    w=Rectangle(a,b)
    print(w.area())
elif x==2:
    a = int(input("Enter the side "))
    y=Square(a)
    print(y.area())
