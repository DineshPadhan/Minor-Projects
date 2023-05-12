def coverter(word):
    def uppercase():
        wd = word()
        return wd.upper()
    return uppercase


def getline():
    return input("Enter a line: ")

res = coverter(getline)
print(res())