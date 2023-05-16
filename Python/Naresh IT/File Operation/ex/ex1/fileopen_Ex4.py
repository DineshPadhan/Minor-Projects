try:
    with open("sample2.txt", "w") as dp:
        print(f'File Type = {type(dp)}')
        print("file open successfully.")
except FileNotFoundError:
    print("File Not Found.")
