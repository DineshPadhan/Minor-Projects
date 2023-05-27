# program for createing csv file using python
import csv
hname = ["empno",'name','sal','pos']
records = [[10, "RS", 300000, "Author"],[20, "TR", 500000, "Scientist"]]

try:
    with open("emp.csv", "a") as fp:
        csvwr = csv.writer(fp)
        #here we write header name to the file name
        csvwr.writerow(hname)
        csvwr.writerows(records)
        print("CSV file created and data saved")
except FileNotFoundError:
    print("File Not found")