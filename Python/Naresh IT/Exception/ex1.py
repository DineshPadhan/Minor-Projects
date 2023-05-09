print("Program Execution start: ")
a = 10
b = 0
print(f'a = {a} b = {b}')
try:
    c = a/b
    print(f'Div({a},{b}) = {c}')
finally:
    print("program execution ended")
    if a==0 or b == 0:
        print("Zero is not divisible")