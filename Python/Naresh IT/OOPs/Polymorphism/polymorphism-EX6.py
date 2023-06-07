class Circle:
    def area(self):
        self.r = float(input("Enter The Radius:"))
        self.ac = 3.14*self.r**2
        print(f'Area of circle is {self.ac}')

class Square:
    def area(self):
        self.s = float(input("Enter The Side:"))
        self.sa = self.s ** 2
        print(f'Area of circle is {self.sa}')
        super().area()

class Rectangle(Square,Circle):
    def area(self):
        self.l = float(input("Enter The Length:"))
        self.b = float(input("Enter The Breadth:"))
        self.ar = self.l * self.b
        print(f'Area of circle is {self.ar}')
        super().area()

r = Rectangle()
r.area()