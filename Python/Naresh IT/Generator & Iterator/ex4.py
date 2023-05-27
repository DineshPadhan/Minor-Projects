a = ("Ram",23,12+3j, True, 23.2)
tple = iter(a)
print(type(tple))
print(tple)
try:
    while True:
        print(next(tple))
except StopIteration:
    print("-"*30)