n=input("Enter The Number: ")
if int(n)<0:
    print("{} is invalid input.".format(n))
else:
    # arr = [int(x) for x in n]
    print(sum([int(x) for x in n]))