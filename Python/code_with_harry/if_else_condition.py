import getpass
# # IF-ELSE STATEMENT
# x=int(input("Enter The Age: "))
#     #Conditional Operator =>"==, <, >, <=, >=, !="
# if(x>=18):
#     print("You are Eligible for vote")
# else:
#     print("You are not eligible for vote")

# # IF-ELSE-IF STATEMENT(ELIF)
# a=int(input("Enter First number: "))
# b=int(input("Enter Second number: "))
# if(a<b):
#     print(a,"is less than",b)
# elif(a>b):
#     print(a,"is greater than",b)
# else:
#     print(a,"is equal to",b)

# NESTED IF CONDITION
id_pass = {
    'user123': 'password123',
    'dinesh': 'dinesh123',
    'anmol': 'anomol123',
    'ramraj': 'Raj123'
}


input_id = input("Enter The Id: ")
input_pass = getpass.getpass('Enter your password: ',"*")
if input_id in id_pass:
    if (id_pass[input_id]==input_pass):
        print("Congratulation ")
    else:
        print("Enter Valid Password")
else:
    print("Enter Correct Id and Password")