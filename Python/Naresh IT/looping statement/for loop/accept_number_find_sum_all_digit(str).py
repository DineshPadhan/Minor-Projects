n=input("Enter The Number: ")
if int(n)<0:
    print("{} is invalid input.".format(n))
else:
    t=0
    for x in n:
       x=int(x)
       t=t+x
    print(t)