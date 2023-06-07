class c1:
    def __init__(self):
        print("C1-----Display()")
class c2(c1):
    def __init__(self):
        print("C2------Display()")
        # super().__init__()
class c3(c2):
    def __init__(self):
        print("C3------Display()")
        # super().__init__()
        c2.__init__(self)
        c1.__init__(self)

o2 = c3()       #object overriden and called