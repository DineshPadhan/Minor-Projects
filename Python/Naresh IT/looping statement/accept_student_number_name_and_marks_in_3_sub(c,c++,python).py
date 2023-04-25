roll = int(input("Enter The Roll number: "))
name = input("Enter The Name: ")
sub = {"C\t":0,"C++\t":0,"Python":0}
for i in sub:
    mark = float(input("Enter The mark of {}: ".format(i)))
    sub[i] = mark
tot = 0
for j in sub:
    tot += sub[j]
per = (tot/300)*100
grade = ""
fail = ""
for k in sub:
    if sub[k]<40:
        fail = "Failed"
if tot<300 and tot>=250:
    grade = "Distinction"
elif tot<249 and tot>=200:
    grade = "Best"
elif tot<199 and tot>=150:
    grade = "Good"
elif tot<149 and tot>=100:
    grade = "Average"
else:
    grade = "Bad"

print("="*18,"Report Card","="*19)
print("Name: {}\t\t\t\t\t\tRoll No.: {}".format(name,roll))
print("="*50)
for i in sub:
    print("\t\t{}\t: {}".format(i,sub[i]))
print("-"*50)
print("Total marks : %0.2f\t\tPercentage : %0.2f"%(tot,per))
print("-"*50)
print("Remark")
print("-"*10)
print("You are a {} Student".format(fail or grade))
print("="*50)
