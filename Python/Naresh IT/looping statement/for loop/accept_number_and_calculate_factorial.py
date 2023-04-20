n=int(input("Enter The Number: "))
if n<0:
    print("{} is invalid input.".format(n))
else:
    f=1
    for x in range(n,0,-1):
        f=f*x
    else:
        print("Factorial of {} is {}".format(n,f))