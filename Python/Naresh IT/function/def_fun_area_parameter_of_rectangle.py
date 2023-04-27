def circlearea():
    h = float(input("Enter  The Height: "))
    b = float(input("Enter  The Base: "))
    res = h*b
    print("area({},{}) = {}".format(h,b, res))
    input()


def circleperimeter():
    h = float(input("Enter  The Height: "))
    b = float(input("Enter  The Base: "))
    res = 2*(h+b)
    print("Perimeter({},{}) = {}".format(h,b, res))
    input()


def menu():
    print("=" * 50)
    print("\t1. Area Rectangle\n\t2. Perimeter Rectangle\n\t3.Exit")
    print("=" * 50)

while True:
    menu()
    ch = int(input("Enter The Choice: "))
    match ch:
        case 1:
            circlearea()
        case 2:
            circleperimeter()
        case 3:
            print("Thanks For Using This Application")
            exit()
        case _:
            print("Your Choice is wrong.")
            print("Try Again...")
