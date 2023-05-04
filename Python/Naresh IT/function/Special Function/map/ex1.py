def incsal(n):
    return (n+(n*(50/100)))
# lst = [-1,3,2,-4,5,-2,1,9,-6,-9]
print("Enter value by separating the value using space: ")
lst = [int(val) for val in input().split()]
polst = list(map(incsal,lst))
print("Incremented Salary: ",polst)