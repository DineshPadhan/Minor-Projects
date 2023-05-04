more3 = lambda w:len(w)>3
nomore3 = lambda w:len(3)<3
line = input("Enter line of Text: ").split()
w1 = list(filter(more3,line))
w2 = list(filter(nomore3,line))
print("More than 3 words: ",w1)
print("Nomore than 3 words: ",w2)
