word=input("Enter the word: ")
result = "Palindrome" if word==word[::-1] else "Not Palindrome"
print("{} is {}".format(word,result))