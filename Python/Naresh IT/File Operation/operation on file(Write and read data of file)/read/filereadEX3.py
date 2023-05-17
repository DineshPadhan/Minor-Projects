# random Access from file
with open("addr1.data","r") as fp:
    print("-"*30)
    print("Initial Pos of fp=", fp.tell())      #0
    filedata = fp.read(15)                      #Name: Dinesh Pa
    print("File Data=", filedata)
    print("-"*30)
    print("Initial Pos of fp=", fp.tell())      #15
    filedata = fp.read(5)                       #dhan
    print("File Data=", filedata)
    print("-"*30)
    print("Initial Pos of fp=", fp.tell())      #21
    filedata = fp.read()                       #dhan
    print("File Data=", filedata)
    print("-"*30)
    print("Initial Pos of fp=", fp.tell())      #21
    print("-"*30)
