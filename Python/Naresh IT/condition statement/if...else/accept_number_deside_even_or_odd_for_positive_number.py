n=int(input("Enter The Number: "))
if n>0:
    if n%2==0:
        print("{} is even".format(n))
    else:
        print("{} is odd.".format(n))
else:
    print("Enter the Positive number.")