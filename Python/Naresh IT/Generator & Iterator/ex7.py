from sys import getsizeof
s = "PYTHON"
siter = iter(s)
print(getsizeof(s))
for val in siter:
    print(val)
    print(getsizeof(val))
