class c1:
    def dis(self):
        print("C1-----Display()")
class c2(c1):
    def dis(self):
        super().dis()
        print("C2-----Display()")
class c3(c2):
    def dis(self):
        super().dis()
        print("C3-----Display()")

o3 = c3()
o3.dis()