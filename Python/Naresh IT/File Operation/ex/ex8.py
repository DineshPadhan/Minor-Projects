try:
    with open("Stud2.data","x+") as fp:
        print("="*50)
        print("file open successfully.")
        print("="*50)
        print("File Name = ",fp.name)
        print("File opening mode = ",fp.mode)
        print("is this file readable = ",fp.readable())
        print("is this file writable = ",fp.writable())
        print("is this file closed = ",fp.closed)
        print("="*50)
    print("="*30,"File is closed","="*30)
    print("is this file closed = ",fp.closed)
except FileExistsError:
    print("File already exist.")