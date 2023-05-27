import csv
record = [76,"Dinesh",0.0,"Student"]

while True:
    eno = int(input("Enter The Employee No. : "))
    ename = input("Enter The Employee Name: ")
    sal = int(input("Enter The Employee salary: "))
    pos = input("Enter The Employee Position: ")
    lst = list()
    lst.append(eno)
    lst.append(ename)
    lst.append(sal)
    lst.append(pos)
    try:
        with open("emp.csv", "a") as fp:
            csvwr = csv.writer(fp)
            csvwr.writerow(record)
            csvwr.writerow(lst)
    except FileNotFoundError:
        print("File Not found")

    ch = input("Do you want to add more data(Yes/No): ").lower()
    if ch=="no":
        break