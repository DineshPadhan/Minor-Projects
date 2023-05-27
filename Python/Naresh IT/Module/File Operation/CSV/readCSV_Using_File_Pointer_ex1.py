# program for reading data from csv file by using file pointer(Normal File)
try:
    with open("data.csv", "r") as fp:
        filedata = fp.read()
        print(filedata)
except FileNotFoundError:
    print("File Not found")