while True:
    age = int(input("Enter The Age: "))
    if age >= 18 and age <=100:
        print("You are eligible for vote.")
        break
    print("You are not eligible for vote.")
    print("{} is Invalid age.".format(age))