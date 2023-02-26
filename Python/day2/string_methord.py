name = "   !!!Hello Developer!!!       "  # Stings Are Immutable
a = "   !!!Hello Developer!!!"  # Stings Are Immutable
b = "!!!Hello Developer!!!      "  # Stings Are Immutable

# print(name.upper())
# print(name.lower())
# print(name.capitalize())  #make capital of first character and rest in small
# print(name.strip())     #remove space from start and end
# print(a.rstrip("!"))    #remove right trailing character i.e that is remove '-,*,! and etc' only remove right sides not started
# print(b.lstrip("!"))    #remove left trailing character i.e that is remove '-,*,! and etc' only remove right sides not started
# print(name.replace("!","*"))    #replace("what to", "what you do")
# print(name.split( ))    #This method splits the given string at the specified instance and returns the separated strings as list items.
# print(name.center(50))    #This method aligns the string to the center as per the parameters given by the user.
# print(name.center(50,"."))  #It will fill the rest of the fill characters provided by the user.
# print(name.count("!"))    #it count the given character
# print(name.endswith(" "))        #This method checks if the string ends with a given value. If yes then return True, else return False.
# print(name.endswith("ev", 13,15))   #We can even also check for a value in-between the string by providing start and end index positions.
# print(name.find("elo"))    #The find() method searches for the first occurrence of the given value and returns the index where it is present.
# print(name.find("dis"))     #If given value is absent from the string then return -1.
# print(name.index("elo"))      #The index() method searches for the first occurrence of the given value and returns the index where it is present.
# print(name.index("dis"))      #If given value is absent from the string then raise an exception.

c = "dbdakcak23jkc8934  "
# print(c.isalnum())      #if A-Z,a-z,0-9 available then true else false
# print(c.isalpha())      #if A-Z,a-z available then true else false
# print(c.islower())      #if all character are in lower then true else false
# print(c.isprintable())      #if any type of non printable character(i.e. \n, \t, etc) are present then false else true

d = "         "
# print(d.isspace())      #if space are used using spacebar or tab then true else false

e = "World Health Organization"
# print(e.istitle())   #if the first letter of each word of the string is capitalized then true else false

f = "WORLD HEALTH ORGANIZATION"
# print(f.isupper())   # if all the characters in the string are upper case then true else false

g = "Python is a Interpreted Language"
# print(g.startswith("Python"))    #if the string starts with a given value then true else false

h = "Python is a Interpreted Language"
# if character is in smaller then swap to capital else swap to smaller
print(h.swapcase())

i = "His name is Dan. Dan is an honest man."
print(i.title())  # it capitalizes each letter of the word within the string.
