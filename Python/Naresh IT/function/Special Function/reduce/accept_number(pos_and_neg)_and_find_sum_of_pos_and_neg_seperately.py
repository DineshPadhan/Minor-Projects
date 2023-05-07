import functools

print("Enter Value with space: ")
num=[int(val) for val in input().split()]

posnum = list(filter(lambda x:x>0,num))
negnum = list(filter(lambda x:x<0,num))
possum = functools.reduce(lambda x,y:x+y,posnum)
negsum = functools.reduce(lambda x,y:x+y,negnum)
print("Positive_Sum({}) = {}".format(posnum,possum))
print("Negitive_Sum({}) = {}".format(negnum,negsum))
