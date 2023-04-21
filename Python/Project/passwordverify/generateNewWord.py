import random
from cryptography.fernet import Fernet
key = Fernet.generate_key()     #generate key
# print(key)
fernet = Fernet(key)            #create a Fernet object with the key
# print(fernet)

def createword(word):
    allword = list()

    # read word in decrypt_password file
    with open("decrypted_password.txt", "r") as file:
        readword = file.read()
    if readword == "":
        generatedword=""
    else:
        generatedword = readword


    word = list(word)
    allword += word
    for ele in allword:
        generatedword+=ele
        generatedword=''.join(random.sample(generatedword,len(generatedword)))

    # encrypt data
    encrypted_word = fernet.encrypt(generatedword.encode())
    # decrypt the word
    decrypted_word = fernet.decrypt(encrypted_word).decode()

    # write generated word in password file
    with open("decrypted_password.txt", "w") as file:
        file.write(decrypted_word)

    # write generated word in password file
    with open("encrypted_password.txt", "wb") as file:
        file.write(encrypted_word)

    # print("orginal Word is {}".format(generatedword))
    # print("Encript data is {}".format(encrypted_word))
    # print("Decrypt word is {}".format(decrypted_word))
    print("New Generated Password is: {}".format(decrypted_word))

def decrypte_password(encrypte):
    decrypte = fernet.decrypt(encrypte).decode()
    print(decrypte)
    return decrypte
def encriptionket():
    return key
