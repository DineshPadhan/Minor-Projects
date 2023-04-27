def circlearea():
    r = float(input("Enter  The Radius: "))
    res = 3.14 * r * r
    print("area({}) = {}".format(r, res))
    input()


def circleperimeter():
    r = float(input("Enter  The Radius: "))
    res = 2 * 3.14 * r
    print("Perimeter({}) = {}".format(r, res))
    input()


def menu():
    print("=" * 50)
    print("\t1.Circle Area\n\t2.Circle Perimetr\n\t3.Exit")
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
