x=int(input("Enter the Day Number: "))
match x:
    case 1:
        print("Its Sunday")
    case 2:
        print("Its Monday")
    case 3:
        print("Its Tuesday")
    case _ if x / 4 == 1:       #we can use condition in the cases and multiple cases also && "_" is use for Default Value
        print("Its Wednesday")
    case 5:
        print("Its Thursday")
    case 6:
        print("Its Friday")
    case 7:
        print("Its Saturday")
    case _:
        print("Wrong Input")