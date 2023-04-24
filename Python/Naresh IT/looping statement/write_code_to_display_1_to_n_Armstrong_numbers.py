# Program to check Armstrong numbers in a certain interval

lower = int(input("Enter The Starting Number: "))
upper = int(input("Enter The Ending Number: "))

for num in range(lower, upper + 1):
    lst = list()
    l = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** l
        temp //= 10
    if num == sum:
        print(num)

