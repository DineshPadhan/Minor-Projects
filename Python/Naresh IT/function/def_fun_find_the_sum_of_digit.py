def sum(n):
    num = n
    tot = 0
    while n>0:
        res = n%10
        tot = tot+res
        n = n//10
    print("Sum({}) = {}".format(num,tot))

num = int(input("Enter The Number: "))
sum(num)