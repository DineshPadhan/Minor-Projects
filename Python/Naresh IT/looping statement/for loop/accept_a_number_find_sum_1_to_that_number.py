n=int(input("Enter The Number: "))
if n<0:
    print("{} is invalid input.".format(n))
else:
    j = int(n/2)
    for i in range(1, j+1):
        if n%i == 0:
            print(i)
    else:
         print(n)