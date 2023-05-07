import functools

print("Enter word with comma: ")
words=[word.strip() for word in input().split(',')]

sen =functools.reduce(lambda x,y:x+' '+y,words)
print(sen)