class Circle:
    def __init__(self):
        self.r = float(input("Enter The Radius:"))
        self.ac = 3.14*self.r**2
        print(f'Area of circle is {self.ac}')

class Square:
    def __init__(self):
        self.s = float(input("Enter The Side:"))
        self.sa = self.s ** 2
        print(f'Area of circle is {self.sa}')
        super().__init__()

class Rectangle(Square,Circle):
    def __init__(self):
        self.l = float(input("Enter The Length:"))
        self.b = float(input("Enter The Breadth:"))
        self.ar = self.l * self.b
        print(f'Area of circle is {self.ar}')
        super().__init__()

r = Rectangle()