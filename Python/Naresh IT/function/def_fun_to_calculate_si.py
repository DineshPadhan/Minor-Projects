def simpleint():
    print("=" * 50)
    p = float(input("Enter the principle Value: "))
    t = float(input("Enter the Time: "))
    r = float(input("Enter the rate of interest: "))
    simple = (p*t*r)/100

    tot = p + simple
    return p, t, r, simple, tot


result = simpleint()
print("Principle Value = {}".format(result[0]))
print("Time Taken = {}".format(result[1]))
print("Rate of Intrest = {}".format(result[2]))
print("Simple Interest = {}".format(result[3]))
print("Total Amount to pay = {}".format(result[4]))
print("="*50)
