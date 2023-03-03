# name = "Dinesh"
# j=0
# for character in name:
#     print(character)
#     j+=1
# print(j)

# data = """hello,
# this is Dinesh.
# i am from Odisha."""
# print(data)
# i=0
# for character in data:
#     print(character)
#     i=i+1
# print(i)

# for i in range(100):    #we can also write range(0,100), where i is initialization, 0 is the start loop, 100 is the end loop and one more thing is in there that is step (default is 1), 
#     print(i)

# for i in range(0, 10, 2):
#     print(i, end=", ")  # Output: 0 2 4 6 8

# my_list = list(range(5))
# print("\n",my_list)  # Output: [0, 1, 2, 3, 4]

# even_numbers = list(range(0, 10, 2))
# print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# for i in range(10, 0, -1):
#     print(i, end=", ")  # Output: 10 9 8 7 6 5 4 3 2 1


# my_list = ['apple', 'banana', 'orange']
# for fruit in my_list:
#     print(fruit, end=", ")    #output: apple, banana, orange, 

# my_tuple = (1, 2, 3)
# for num in my_tuple:
#     print(num, end=", ")    #1, 2, 3, 

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, value in my_dict.items():
#     print(key,":",value)

# my_set = {1, 2, 3}
# for num in my_set:
#     print(num, end=", ")    #Output: 1, 2, 3, 

# line_num = 1
# word_count = 0
# with open('myfile.txt', 'r') as f:
#     for line in f:
#         print(line_num, end=": ")                         #it print all the line number
#         print(line)                                       #it print all the line 
#         line_num += 1
#         words = line.split()                              #it is for splitting word from the line
#         word_count += len(words)                          #it is counting the total word                         
# print("Total Word used in the file is:",word_count)       #it print the total word