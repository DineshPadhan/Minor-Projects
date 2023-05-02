big = lambda a,b: a if a>b else b if a<b else "Both same"
a=int(input("Enter Num1: "))
b=int(input("Enter Num2: "))
print("Big({},{}) = {}".format(a,b,big(a,b)))