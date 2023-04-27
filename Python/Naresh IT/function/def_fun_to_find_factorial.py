def factotial(n):
    if n<0:
        return "{} is a negative value and negative value dont have factorial".format(n)

    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
n = int(input("Enter Number To find Factorial: "))
print("fact({}) = {}".format(n,factotial(n)))