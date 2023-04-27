def palindrom(n):
    rev = n[::-1]
    if n==rev:
        print("{} is a Palindrome Number".format(n))
    else:
        print("{} is not a Palindrome Number".format(n))

num = input("Enter The number: ")
palindrom(num)