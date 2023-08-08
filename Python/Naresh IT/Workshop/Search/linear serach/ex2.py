def linarSearch(lst,skey):
    lst1 =[]
    for i in range(len(lst)):
        if lst[i] == skey:
            lst1.append(i)
    return lst1
lst = [6,1,3,6, 5,6,9,6,7,8]
skey = 6
lst1 = linarSearch(lst,skey)
if len(lst1) == 0:
    print(f'{skey} is not found')
else:
    print(f'{skey} is found {len(lst1)} times')
    print(f"The indexes are: ",end="")
    for i in lst1:
        print(i,end=" ")