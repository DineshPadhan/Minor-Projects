# student pickling data

import pickle
with open("data.txt","ab") as fp:
   while True:
        #read std value from Keybord
        sno = int(input("Enter Student Number: "))
        sname = input("Enter Student Name: ")
        mark = int(input("Enter Student Marks: "))
        l = list()
        l.append(sno)
        l.append(sname)
        l.append(mark)
        # save list obj content as a record to the file
        pickle.dump(l,fp)
        print("-"*30)
        print("Student data saved as Record")
        print("-"*30)
        ch = input("Do You want to enter yes or no: ").lower()
        if ch == "no":
            break