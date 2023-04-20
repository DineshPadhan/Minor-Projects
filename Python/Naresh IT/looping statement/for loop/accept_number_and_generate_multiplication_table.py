num=int(input("Enter Number: "))
if num > 0:
    for x in range(1,11):
        print("{} * {} = {}".format(num,x,num*x))
else:
    print("{} is invalid input.".format(num))