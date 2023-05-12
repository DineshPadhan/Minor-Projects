def coverter(word):
    def uppercase():
        wd = word()
        return wd.upper()
    return uppercase


@coverter
def getline():
    return input("Enter a line: ")

res = getline()
print(res)