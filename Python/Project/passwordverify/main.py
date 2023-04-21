import generateNewWord
# import cryptography.fernet
#
# # Key from that generated encription
# key = generateNewWord.encriptionket()
# # print(key)
# # Create a Fernet object using the key
# fernet = cryptography.fernet.Fernet(key)

# read word in decrypt_password file
with open("decrypted_password.txt", "rb") as file:
    decrypted_word = file.read().decode()
    print("Original Password is: ",decrypted_word,end="")
# orginalpassword = generateNewWord.decrypte_password(encrypted_word)
# print(orginalpassword)

# input password
password=input("\nEnter the Password: ")
temp=password
if (password == decrypted_word):
    print("Access Granted")
else:
    if decrypted_word!="":
        print("{} is Wrong Password".format(temp))
    generateNewWord.createword(password)
