try:
    a = int(input("Enter first value:"))
    b = int(input("Enter Seconf value:"))
    c = a/b
    # s = "Python"
    # print(s[11])
except ZeroDivisionError as z:
    # print(z)
    print("Dont enter Zero as denominator.")
except ValueError as v:
    print(v)
    print("Dont enter Alpha Numeric, symbol etc...")
# except:
#     print("Oops... something went wrong.")  # not recommended form but it recommended to write at last for any other type of error
else:
    print(f'Division = {c}')
finally:
    print("I am From Finally block")
