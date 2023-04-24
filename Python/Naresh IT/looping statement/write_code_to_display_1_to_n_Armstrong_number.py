n = int(input("Enter The Number: "))
if n>0:
    temp = n
    temp=str(temp)
    l = len(temp)
    temp=int(temp)
    tot = 0
    res = 0
    while(temp>0):
        res = temp%10
        tot = tot+(res**l)
        temp=temp//10
    if n == tot:
        print("{} is a Armstrong number.".format(n))
    else:
        print("{} is not a Armstrong number.".format(n))
else:
    print("{} is invalid input".format(n))