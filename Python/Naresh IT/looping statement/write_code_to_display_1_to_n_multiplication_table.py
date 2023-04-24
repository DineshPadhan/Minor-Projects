n = int(input("Enter The Number: "))
if n>0:
    for x in range(1, n + 1):
        print("Multiplication Table of {} is: ".format(x))
        for y in range(1, 11):
            print("{} * {} = {}".format(x, y, x * y))
        print("=" * 50)
else:
    print("{} is invalid input".format(n))