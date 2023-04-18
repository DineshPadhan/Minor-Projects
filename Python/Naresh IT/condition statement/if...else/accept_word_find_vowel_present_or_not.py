word=input("Enter The word: ")
if ("a"in word.lower() or "e" in word.lower() or "i" in word.lower() or "o" in word.lower() or "u" in word.lower()):
    print("{} is Vowel Word.".format(word.title()))
else:
    print("{} is not Vowel word.".format(word.title()))