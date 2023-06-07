class c1:
    def dis(self):
        print("C1-----Display()")
class c2(c1):
    def dis(self):
        c1.dis(self)
        print("C2-----Display()")
class c3(c2):
    def dis(self):
        c2.dis(self)
        print("C3-----Display()")

o3 = c3()
o3.dis()