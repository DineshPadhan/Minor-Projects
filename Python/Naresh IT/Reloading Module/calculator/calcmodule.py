def addop():
    print("Enter two value for Addition")
    a,b = int(input()),int(input())
    print("Add({},{}) = {}".format(a,b,a+b))
def subop():
    print("Enter two value for Subtraction")
    a,b = int(input()),int(input())
    print("Sub({},{}) = {}".format(a,b,a-b))
def mulop():
    print("Enter two value for Multiplication")
    a,b = int(input()),int(input())
    print("Mul({},{}) = {}".format(a,b,a*b))
def divop():
    print("Enter two value for Division")
    a,b = int(input()),int(input())
    print("Division({},{}) = {}".format(a,b,a/b))
def fdivop():
    print("Enter two value for Floor Division")
    a,b = int(input()),int(input())
    print("Floor Division({},{}) = {}".format(a,b,a//b))
def moddivop():
    print("Enter two value for Modulo Division")
    a,b = int(input()),int(input())
    print("Modulo Division({},{}) = {}".format(a,b,a%b))
def exop():
    a,b = int(input("Enter Base: ")),int(input("Enter The power: "))
    print("Exponentiation({},{}) = {}".format(a,b,a**b))