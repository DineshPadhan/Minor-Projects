language_dict = {1: "English",2: "French",3: "Spanish",4: "German",5: "Italian",6: "Russian",7: "Chinese",8: "Japanese",9: "Korean",10: "Arabic"}
key = 70
val = language_dict.get(key)
if val != None:
    print(f'{key} ===> {val}')
else:
    print(f'{key} is not found')