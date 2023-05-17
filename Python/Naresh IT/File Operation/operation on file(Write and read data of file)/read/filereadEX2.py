with open("../write/verysmall1.data","r") as fp:
    filedata = fp.readlines()
    for fd in filedata:
        print(fd)
    print(type(filedata))