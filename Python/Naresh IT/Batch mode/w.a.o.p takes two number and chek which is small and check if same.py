first_number = int(input("Enter The First value: "))
second_number = int(input("Enter The Second value: "))
third_number = int(input("Enter The Third value: "))
# condition
# result = first_number if first_number>=second_number and first_number>third_number else second_number if first_number<second_number and second_number>=third_number else third_number if first_number<=third_number and second_number<third_number else "Value is same"
result = first_number if third_number>first_number<=second_number else second_number if first_number>second_number<=third_number else third_number if first_number>=third_number<second_number else "All value are same"
print("big({},{},{}) = {}".format(first_number,second_number,third_number,result))