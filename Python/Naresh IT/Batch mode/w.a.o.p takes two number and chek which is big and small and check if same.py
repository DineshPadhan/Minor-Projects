first_number = int(input("Enter The First value"))
second_number = int(input("Enter The Second value"))
# condition
result = first_number if first_number>second_number else second_number if first_number<second_number else "Value is same"
print("big({},{}) = {}".format(first_number,second_number,result))