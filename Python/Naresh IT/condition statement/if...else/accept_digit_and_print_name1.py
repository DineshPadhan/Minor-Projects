dic={"0":"Zer0","1":"One","2":"Two","3":"Tree","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine",".":"Dot","-":"Negative"}
num=input("Enter Number: ")
for x in num:
    res=dic.get(x)
    if res!=None:
        print(res,end=" ")
    else:
        print("\nWrong Input.")
        exit()