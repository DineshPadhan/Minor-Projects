lst = [1,2,3,-1,-4,-5,-6,0,5,7,-3]
res = [val if val>=0 else lst.remove(val) for val in lst]
print(res)