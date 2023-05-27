import csv
with open("emp.csv", "r") as fp:
    csvwr = csv.DictReader(fp)
    print(csvwr)
    print("-" * 30)
    for drdata in csvwr:
        # print(drdata)
        for dict,val in drdata.items():
            print(dict+"\t"+val)
        print("-"*30)