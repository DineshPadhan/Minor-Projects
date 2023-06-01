class Student:
    @classmethod
    def collage(cls):
        Student.clg = "OU"
        Student.sub = "BCA"
        cls.collageAddr()
    @classmethod
    def collageAddr(cls):
        Student.addr = "Hyderabad"
    def inputdata(self):
        self.sno=int(input("Enter The No.: "))
        self.sname = input("Enter The Name: ")
        self.mark = float(input("Enter The marks: "))
        self.outputdata()
    def outputdata(dinesh):
        Student.collage()       # Calling class Level method
        for x,y in dinesh.__dict__.items():
            print(f'{x} ===> {y}')
        print(f'Collage ==> {dinesh.clg}')
        print(f'Subject ==> {dinesh.sub}')
        print(f'Address ==> {dinesh.addr}')
s1=Student()
# s1.collage()      # TCalling class Level method
s1.inputdata()
print("-----------------------------")
s2=Student()
s2.inputdata()