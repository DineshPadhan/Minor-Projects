word=input("Enter the Word: ")
if word==word[::-1]:
    print("{} is a Palindrome word.".format(word))
if word!=word[::-1]:
    print("{} is Not Palindrome word.".format(word))