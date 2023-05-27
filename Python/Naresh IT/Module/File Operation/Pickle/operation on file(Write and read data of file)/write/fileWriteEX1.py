# program for writing the data to the file

with open("verysmall.data", 'w') as fp:
    fp.write("100")
    fp.write("Dinesh")
    fp.write("11.5")
    print("Data write successfully")