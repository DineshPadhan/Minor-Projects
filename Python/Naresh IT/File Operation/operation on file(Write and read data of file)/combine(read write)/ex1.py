with open("dynamic.data","a+") as fp:
    while True:
        name = input("Enter Your Name: ").capitalize()
        if name !="@":
            fp.write("Name: "+ name+"\n")
        else:
            break
with open("dynamic.data","r") as fd:
    fdata = fd.readlines()    # this is used to make a list of all line in that file
    # print(fdata)
    for fdt in fdata:
        print(fdt,end="")