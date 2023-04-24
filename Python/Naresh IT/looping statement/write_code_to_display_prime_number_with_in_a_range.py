n1 = int(input("Enter The Starting Number: "))
n2 = int(input("Enter The Ending Number: "))
if n1>1 and n2>0 and n1<n2:
    lst = list()
    for x in range(n1, n2+1):
            for i in range(2,x):
                if x%i==0:
                    break
            else:
                lst.append(x)
    # print(lst)
    # print(len(lst))
    print("="*100)
    print("Prime number between {} and {} is: ".format(n1,n2),end="")
    for num in lst:
        print(num,end=" ")
    print()
    print("="*100)
else:
    print("="*50)
    if n1<2:
        print("Starting Number {} is invalid input".format(n1))
    if n2<1:
        print("Ending Number {} is invalid input".format(n2))
    if n1>n2:
        print("Starting Value is Not less than Ending value")
    print("="*50)