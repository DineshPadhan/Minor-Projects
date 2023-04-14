number = int(input("Enter The value: "))
result = "Positive" if number>0 else "Negative" if number<0 else "Number is Zero"
print("{} is {}".format(number,result))