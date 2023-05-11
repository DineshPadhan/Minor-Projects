# write a code for generate multiplication table where n must be the positive number. if n=0 then raise ZerroError. If n>0 then raise NegitavieNumberError
class ZerroError(Exception):pass
class NegitavieNumberError(BaseException):pass

try:
    n = int(input("Enter the Multiplicatable number: "))
    if n==0:
        raise ZerroError
    elif n<0:
        raise NegitavieNumberError
    else:
        for i in range(1,11):
            print(f'{n} * {i} = {n*i}')
except ZerroError:
    print("Don't enter zero as Multiplication Table")
except NegitavieNumberError:
    print("Don't enter Negative number as Multiplication Table")
except ValueError:
    print("Dont enter Alpha Numeric, symbol etc...")
except :
    print("Something went error")