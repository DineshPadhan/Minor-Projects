# icici.py--File Name and Module name
bname = "ICICI"
addr = "HYD"  # here bname and addr are called Global Variables


def simpleint():  # Function definition
    p = float(input("Enter Principle Amount:"))
    t = float(input('Enter Time:'))
    r = float(input("Enter rate of interest:"))
    # cal si and totamt  to pay
    si = (p * t * r) / 100
    totamt = p + si
    print("*" * 50)
    print("Simple Interest Calculations")
    print("*" * 50)
    print("\tPrinciple Amount:{}".format(p))
    print("\tTime:{}".format(t))
    print("\tRate of Interest:{}".format(r))
    print("\tSimple Interest:{}".format(si))
    print("\tTOTAL AMOUNT TO PAY:%0.2f" % totamt)
    print("*" * 50)
