from builtins import input


def ca():
    print("Enter radius of Circle: ")
    a = int(input())
    print("Area of Circle({}) = {}".format(a,3.14*a**2))
def cp():
    print("Enter radius of Circle: ")
    a = int(input())
    print("Parameter of Circle({}) = {}".format(a,2*3.14*a))
def sa():
    print("Enter height of Square:")
    a= int(input())
    print("Area of Square({}) = {}".format(a,a*a))
def sp():
    print("Enter height of Square:")
    a = int(input())
    print("Parameter of Square({}) = {}".format(a,4*a))
def ra():
    print("Enter height and breath of Rectangle: ")
    a,b = int(input()),int(input())
    print("Area of Rectangle({},{}) = {}".format(a,b,a*b))
def rp():
    print("Enter height and breath of Rectangle: ")
    a,b = int(input()),int(input())
    print("Parameter of Rectangle({},{}) = {}".format(a,b,2*(a+b)))
def ta():
    print("Enter height and base of Triangle: ")
    a,b = int(input()),int(input())
    print("Area of Triangle({},{}) = {}".format(a,b,a*b/2))
def tp():
    print("Enter all side length of Triangle: ")
    a,b,c = int(input()),int(input()),int(input())
    print("Parameter of Triangle({},{},{}) = {}".format(a,b,c,a+b+c))