a = [12,23,34,54,56,76,78,90,21,32,43,45]
lst = iter(a)
print(type(lst))
print(lst)
try:
    while True:
        print(next(lst))
except StopIteration:
    print("-"*30)