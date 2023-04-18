number1 = int(input("Enter the first digit: "))
number2 = int(input("Enter the Second digit: "))
sym = input("Enter the symbol: ")

print("="*50)
match(sym):
    case "+":
        print("{} + {} = {}".format(number1, number2, number1+number2))
    case "-":
        print("{} - {} = {}".format(number1, number2, number1 - number2))
    case "*":
        print("{} * {} = {}".format(number1, number2, number1 * number2))
    case "/":
        print("{} / {} = {}".format(number1, number2, number1 / number2))
    case "//":
        print("{} // {} = {}".format(number1, number2, number1 // number2))
    case "**":
        print("{}**{} = {}".format(number1, number2, number1 ** number2))
    case "%":
        print("{} % {} = {}".format(number1, number2, number1 % number2))
    case _:
        print("Enter The correct symbol.")
print("="*50)