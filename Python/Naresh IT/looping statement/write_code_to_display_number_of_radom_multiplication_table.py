n = int(input("How many multiplication table you want: "))
if n>0:
    lst = list()
    for x in range(1, n + 1):
        num = int(input("Which {} multiplication table you want: ".format(x)))
        lst.append(num)
    print("Given value: {}".format(lst))
    for i in lst:
        print("Multiplication Table of {} is: ".format(i))
        for j in range(1,11):
            print("{} * {} = {}".format(i,j,i*j))
        print("="*50)
else:
    print("{} is invalid input".format(n))