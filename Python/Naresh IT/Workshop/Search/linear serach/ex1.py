def linarSearch(lst,skey):
    for i in range(len(lst)):
        if lst[i] == skey:
            return i
    return -1
lst = [1,3, 5,6,9,7,8]
skey = 1
index = linarSearch(lst,skey)
if index == -1:
    print(f'{skey} is not found')
else:
    print(f'{skey} is in {index} index')