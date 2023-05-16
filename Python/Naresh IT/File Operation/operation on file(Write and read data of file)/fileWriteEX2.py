# program for writing the data to the file

with open("verysmall1.data",'a') as fp:
    fp.write("="*30)
    fp.write("\nName: Harish sahu\n")
    fp.write("Class: BCA\n")
    fp.write("Address: SR Nagar, Hyderabad\n")
    print("Data write successfully\n")