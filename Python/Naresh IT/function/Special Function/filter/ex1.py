# def positive(n):
#     if n > 0:
#         return True
#     else:
#         return False
positive = lambda n:n>0
negitive = lambda n:n<0
# lst = [-1,3,2,-4,5,-2,1,9,-6,-9]
print("Enter value by separating the value using space: ")
lst = [int(val) for val in input().split()]
polst = list(filter(positive,lst))
nelst = list(filter(negitive,lst))
print("Positive value: ",polst)
print("Negitive value: ",nelst)