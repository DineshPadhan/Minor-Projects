num=input("Enter the number: ")
for x in num:
    if x=="0":
        print("Zero",end=" ")
    elif x=="1":
        print("One",end=" ")
    elif x=="2":
        print("Two",end=" ")
    elif x=="3":
        print("Three",end=" ")
    elif x=="4":
        print("Four",end=" ")
    elif x=="5":
        print("Five",end=" ")
    elif x=="6":
        print("Six",end=" ")
    elif x=="7":
        print("Seven",end=" ")
    elif x=="8":
        print("Eight",end=" ")
    elif x=="9":
        print("Nine",end=" ")
    elif x==".":
        print("Point",end=" ")
    elif x=="-":
        print("Negative",end=" ")
    else:
        print("\nWrong input.")
        exit(0)