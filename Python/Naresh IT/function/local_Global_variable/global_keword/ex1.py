a = 1
b=2
c=3
d=4
def opera():
    a=10
    b=20
    c=30
    d=40
    res = a+b+c+d+globals()["a"]+globals()["b"]+globals()["c"]+globals()["d"]
    print("Operation: {}".format(res))
opera()