vowel = lambda word:"Vowel" if "a" in word.lower() or "e" in word.lower() or "i" in word.lower() or "o" in word.lower() or "u" in word.lower() else "Not a Vowel"
word = input("Enter word: ")
print("{} is {}".format(word,vowel(word)))