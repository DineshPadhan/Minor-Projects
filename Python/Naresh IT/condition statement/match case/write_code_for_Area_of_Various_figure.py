print("Enter The figure Letter as follow")
print("="*50)
print("\tR = Rectangle")
print("\tT = Triangle")
print("\tS = Square")
print("\tC = Circle")
print("="*50)
let = input("Enter The letter: ").upper()
match let:
    case "R":
        print("Rectangle")
        length = float(input("Enter The length: "))
        breath = float(input("Enter The Breath: "))
        print("=" * 50)
        print("Area of Rectangle is %0.2f"%(length*breath))
    case "T":
        print("Triangle")
        height = float(input("Enter The Height: "))
        base = float(input("Enter The Base: "))
        print("=" * 50)
        print("Area of Triangle is %0.2f"%(height*base*0.5))
    case "S":
        print("Square")
        length = float(input("Enter The length: "))
        print("=" * 50)
        print("Area of Square is %0.2f"%(length**2))
    case "C":
        print("Circle")
        radius = float(input("Enter The Radius: "))
        print("=" * 50)
        print("Area of Circle is %0.2f"%(4*3.14*radius))
    case _:
        print("Enter Correct Figure Letter.")
print("="*50)