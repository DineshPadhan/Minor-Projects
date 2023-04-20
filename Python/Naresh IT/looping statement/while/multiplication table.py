num=int(input("Enter Number: "))
if num > 0:
    i=1
    while (i<=10):
        print("{} * {} = {}".format(num,i,num*i))
        i+=1
else:
    print("{} is invalid input.".format(num))