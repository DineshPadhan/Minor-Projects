class calculator:pass


s = calculator()
print("content of calculator: ",s.__dict__)
print("-"*30)
s.a = float(input("Enter num1: "))
s.b = float(input("Enter num2: "))
print("-"*30)
print("content of calculator: ",s.__dict__)
print("-"*30)
s.c = s.a+s.b
print("First value = {}".format(s.a))
print("Second value = {}".format(s.b))
print("Sum = {}".format(s.c))
print("-"*30)
