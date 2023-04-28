words = input("Enter a list of words separated by spaces: ").split()

largest_palindrome = ""
for word in words:
    if word == word[::-1] and len(word) > len(largest_palindrome):
        largest_palindrome = word

if largest_palindrome:
    print("The largest palindrome is:", largest_palindrome)
    print("Its length is:", len(largest_palindrome))
else:
    print("No palindromes found in the list.")
