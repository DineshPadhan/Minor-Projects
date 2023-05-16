# program for writing the data to the file using array

a = {1:101, 2:'Ramraj', 3:'BCA', 4:200000, 5:'SR Nagar,Hyderabad'}
with open("verysmall2.data",'a') as fp:
    fp.writelines(str(a)+"\n")
    print("Data write successfully\n")