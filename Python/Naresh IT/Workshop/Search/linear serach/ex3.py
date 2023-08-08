def linarSearch(lst,index,skey):
    if index == -1:
        return -1
    elif lst[index] == skey:
        return index
    return linarSearch(lst, index-1, skey)
lst = [1,3, 5,6,9,7,8]
skey = 1
index = linarSearch(lst,len(lst)-1,skey)
if index == -1:
    print(f'{skey} is not found')
else:
    print(f'{skey} is in {index} index')