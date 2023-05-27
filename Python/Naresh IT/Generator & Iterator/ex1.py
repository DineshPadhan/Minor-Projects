from sys import getsizeof
def generator(x,y):
    while x<=y:
        yield x
        x+=1
try:
    val = generator(4,10)
    print(getsizeof(val))
    while True:
        j = next(val)
        print(j)
        print(getsizeof(j))

except StopIteration:
    print("----------------")