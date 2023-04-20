sen=input("Enter The Sentense: ")
print("="*50)
if sen=="":
    print("Invalid input.")
else:
    word = sen.split()
    for i in word:
        if i == i[::-1]:
            print("{} is a palindrome word.".format(i))
        else:
            print("{} is not a palindrome word.".format(i))
print("="*50)