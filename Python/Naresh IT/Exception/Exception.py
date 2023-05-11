# develop an exception for handling zerodevisionError program for generating an exception when division by zero taking place. program for bhandeling the exception when zero is the denominator.
class DivisionError(Exception):pass

a = int(input("Enter First value: "))
b = int(input("Enter second value: "))

try:
    if b==0:
        raise DivisionError
    else:
        print("Division is: ",a/b)
except DivisionError:
    print("Don't enter zero as denominator")