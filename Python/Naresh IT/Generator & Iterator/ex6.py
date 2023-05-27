a = {1:"Ram",2:23,3: 12+3j, 4:True, 5:23.2}
sets = iter(a)
print(type(sets))
print(sets)
try:
    for i in sets:
        print("{}---->{}".format(i,a[i]))
except StopIteration:
    print("-"*30)