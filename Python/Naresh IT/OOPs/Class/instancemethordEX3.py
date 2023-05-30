class Student:
    def getstuddata(self):
        print("ID of current getstuddata()=",id(self))
        self.sno = int(input("Enter first student no.: "))
        self.sname = input("Enter First student name: ")
        self.mark = float(input("Enter First student mark: "))
        self.displaydata()
    def displaydata(self):
        print("student number: {}".format(self.sno))
        print("student name: {}".format(self.sname))
        print("student mark: {}".format(self.mark))

s1 = Student()
s2 = Student()
print("-----------------------------")
print("ID of s1 in main programme = ",id(s1))

s1.getstuddata()
print("---------------------")
s2.getstuddata()