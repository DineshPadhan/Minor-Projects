from sys import getsizeof
def generator():
    yield "ram"
    yield "Shyam"
    yield "hari"
    yield "Dinesh"
    yield "karan"
    yield "Ramesh"
val = generator()
print(getsizeof(val))
try:
    while True:
        print("----------------")
        j = next(val)
        print("\t",j)
        print(getsizeof(j))

except StopIteration:
    print()