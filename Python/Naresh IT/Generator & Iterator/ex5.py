a = {"Ram",23,12+3j, True, 23.2}
sets = iter(a)
print(type(sets))
print(sets)
try:
    while True:
        print(next(sets))
except StopIteration:
    print("-"*30)