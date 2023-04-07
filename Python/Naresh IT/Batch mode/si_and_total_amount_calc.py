p=float(input("Enter Principle amount: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate of Interest: "))

si=(p*t*r)/100
tot=p+si

print("-"*30)
print("Simple interest is %0.2f\nTotal Amount is %0.2f"%(si,tot))
print("-"*30)