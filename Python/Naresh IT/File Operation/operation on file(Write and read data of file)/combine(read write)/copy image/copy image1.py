sfile = input("Enter The Coping File Location(D:\Project\FileName.extension): ")
dfile = input("Enter The Coping File Location(C:\Data\CopiedFileName.extension): ")
try:
    with open(sfile,"rb") as rb:
        with open(dfile,"wb") as wb:
            orgnialImg = rb.read()      # Copied the image
            wb.write(orgnialImg)
            print("Image Copied successfully.")
except FileNotFoundError:
    print("File does not found.")