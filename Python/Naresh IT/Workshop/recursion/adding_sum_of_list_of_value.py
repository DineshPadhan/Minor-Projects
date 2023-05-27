def dosum(lst):
    if not lst:
        return 0
    else:
        ans = lst[0] + dosum(lst[1:])
        return ans
lst = [1,2,3,4,5,6,7,8,9,10]
res = dosum(lst)
print(res)