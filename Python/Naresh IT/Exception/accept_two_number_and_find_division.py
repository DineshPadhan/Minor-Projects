try:
    a = int(input("Enter first value:"))
    b = int(input("Enter Seconf value:"))
    c = a/b
except ZeroDivisionError:
    print("Dont enter Zero as denominator.")
except ValueError:
    print("Dont enter Alpha Numeric, symbol etc...")
else:
    print(f'Division = {c}')
finally:
    print("I am From Finally block")