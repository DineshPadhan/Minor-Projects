import csv
hname=["HTNO","NAME","BRANCH","CGPA"]
records = [{'HTNO': 100, 'NAME': 'Azad', 'BRANCH': 'CSE', 'CGPA': 7.5},
    {'HTNO': 200, 'NAME': 'Dinesh', 'BRANCH': 'EEE', 'CGPA': 8.5},
    {'HTNO': 300, 'NAME': 'Hari', 'BRANCH': 'IT', 'CGPA': 7},
    {'HTNO': 400, 'NAME': 'Rahul', 'BRANCH': 'MEC', 'CGPA': 9.3}]
with open("universtud.csv", "a") as fp:
    csvwr = csv.DictWriter(fp,fieldnames=hname)
    csvwr.writeheader()
    # csvwr.writerow(hname)
    csvwr.writerows(records)
    print('Record saved successfully in csv file')