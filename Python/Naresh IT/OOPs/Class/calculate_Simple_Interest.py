class simpleInterest:
    p = float(input("Enter The price: "))
    t = float(input("Enter The Time taking: "))
    r = float(input("Enter The Rate of interest: "))
    si = (p * t * r) / 100


s1 = simpleInterest()
print("Simple interest is: ",s1.si)
print("Amount to pay is: ",s1.p+s1.si)

