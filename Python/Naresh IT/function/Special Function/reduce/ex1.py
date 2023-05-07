import functools
def tot(x,y):
    return x+y
print("Enter Value with space: ")
a=[int(val) for val in input().split()]
res = functools.reduce(tot,a)
print("Sum({}) = {}".format(a,res))