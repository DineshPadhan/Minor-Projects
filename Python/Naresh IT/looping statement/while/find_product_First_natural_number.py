num = int(input("Enter number of product you want: "))
if num<=0:
    print("{} is invalid input".format(num))
else:
    print("="*50)
    print("Product of first {} digit is ".format(num))
    i,tot=1,1
    while (i<=num):
        tot = tot * i
        i += 1
    else:
        print("="*50)
        print(tot)