# program for reading data from csv file by using file pointer(Normal File)
import csv
try:
    with open("universtud.csv", "r") as fp:
        csvr = csv.reader(fp)           # here CSVR is the an object of <class, _csv.reader>
        print(csvr)
        print("-"*30)
        for record in csvr:
            for val in record:
                print(val, end="\t")
                if val=="pos":
                    print("\n","-"*30,end="")
            print()
        print("-"*30)
except FileNotFoundError:
    print("File Not found")