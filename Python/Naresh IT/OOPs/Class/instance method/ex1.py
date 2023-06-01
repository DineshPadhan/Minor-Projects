class Student:
    def inputdata(self):
        self.sno=int(input("Enter The No.: "))
        self.sname = input("Enter The Name: ")
        self.mark = float(input("Enter The marks: "))
        self.outputdata()
    def outputdata(dinesh):
        for x,y in dinesh.__dict__.items():
            print(f'{x} ===> {y}')
s1=Student()
s1.inputdata()
print("-----------------------------")
s2=Student()
s2.inputdata()