try:
    dp = open("sample2.txt", "r")
except FileNotFoundError:
    print("File Not Found.")
else:
    print(f'File Type = {type(dp)}')
    print("file open successfully.")