palindrome = lambda word:"Palindrome"if word ==word[::-1] else "Not Vowel"
word = input("Enter word: ")
print("{} is {}".format(word,palindrome(word)))