class student:
    def std(self):
        self.sname = input("Enter your name: ")
        self.sno = int(input("Enter Your no.: "))
        self.mark = float(input("Enter your mark: "))
class colage:
    def clg(self):
        self.cname = input("Enter your collage name: ")
        self.caddr = input("Enter your collage address: ")
class teacher:
    def tchr(self):
        self.tname = input("Enter your teacher name: ")
        self.tsub = input(f'Mr./Mrs. {self.tname} which Subject teach: ')
class printdata:
    print('----------------------------------------------------------------')
    @staticmethod
    def printall(obj):
        print('----------------------------------------------------------------')
        for x,y in obj.__dict__.items():
            print("\t{}--->{}".format(x,y))

s = student()
c = colage()
t = teacher()

# get value
print("----------------------------------------------------------------")
s.std()
print("----------------------------------------------------------------")
c.clg()
print("----------------------------------------------------------------")
t.tchr()
print("----------------------------------------------------------------")

# print Value
printdata.printall(s)
printdata.printall(c)
printdata.printall(t)