import functools

print("Enter Value with space: ")
a=[int(val) for val in input().split()]

high = functools.reduce(lambda x,y:x if x>y else y,a)
low = functools.reduce(lambda x,y:x if x<y else y,a)

print("Max({}) = {}".format(a,high))
print("Min({}) = {}".format(a,low))