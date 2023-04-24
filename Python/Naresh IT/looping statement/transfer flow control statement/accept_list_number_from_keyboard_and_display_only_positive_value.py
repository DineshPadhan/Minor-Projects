lst = []
while True:
    x=input("Enter value: ")
    if x=="":
        break
    lst.append(int(x))
print("List of +ve value:")
for val in lst:
    if val>0:
        print(val)