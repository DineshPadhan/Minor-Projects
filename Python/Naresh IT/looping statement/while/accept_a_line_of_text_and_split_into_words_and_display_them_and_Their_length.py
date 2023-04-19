sen = input("Enter The Sentence: ")
word = sen.split(" ")
i=0
while (i<=(len(word)-1)):
    print("{}\t{}".format(word[i],len(word[i])))
    i+=1
else:
    print("="*50)