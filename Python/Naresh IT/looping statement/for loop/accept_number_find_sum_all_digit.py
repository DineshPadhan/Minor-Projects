n=int(input("Enter The Number: "))
if n<0:
    print("{} is invalid input.".format(n))
else:
    t=0
    while (n>0):
        rem = n%10
        t=t+rem
        n=n//10
    print(t)