class Circle:
    r = float(input("Enter the Radius of Circle: "))
    a = 3.14*r*r
    p = 2*3.14*r

c=Circle()
print("Area({})={}".format(c.r,c.a))
print("Parameter({})={}".format(c.r,c.p))