n = int(input("Enter The Number: "))
if n>0:
    lst = list()
    for x in range(1, n + 1):
        if n%x==0:
            lst.append(x)
    lst.remove(n)
    print(lst)
    tot=0
    for y in lst:
        tot = tot+y
    if n == tot:
        print("{} is a perfect number.".format(n))
else:
    print("{} is invalid input".format(n))