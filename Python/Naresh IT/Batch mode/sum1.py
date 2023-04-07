a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
sym = input("Enter the symbol for calculate: ")
if(sym=="+"):
    c = a+b
elif(sym=="-"):
    c = a-b
elif(sym=="*"):
    c = a*b
elif(sym=="/"):
    c = a/b
else:
    exit(0)
print("-*"*10, "Output", "*-"*10)
print("Value of a is", a)
print("Value of b is", b)
print("Value of c is", c)