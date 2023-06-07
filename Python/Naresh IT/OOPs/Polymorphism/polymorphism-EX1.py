class c1:
    def dis1(self):
        print("C1-----Display()")
class c2(c1):
    def dis2(self):
        print("C2-----Display()")
class c3(c2):
    def dis3(self):
        print("C3-----Display()")

o3 = c3()
o3.dis1()
o3.dis2()
o3.dis3()