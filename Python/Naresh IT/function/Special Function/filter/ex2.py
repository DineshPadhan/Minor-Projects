print("Enter value by separating the value using space: ")
lst = [int(val) for val in input().split()]
evenlst = list(filter(lambda n:n%2==0,lst))
oddlst = list(filter(lambda n:n%2!=0,lst))
print("Even List: ",evenlst)
print("Odd List: ",oddlst)