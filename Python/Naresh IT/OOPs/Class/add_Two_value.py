class Add:
    def readval(self):
        self.a = float(input("Enter First no. : "))
        self.b = float(input("Enter Second no. : "))
        self.addval()
    def addval(self):
        self.c = self.a+self.b
        self.disval()

    def disval(self):
        print("First val: ",self.a)
        print("Second val: ",self.b)
        print("Sum({},{})={}".format(self.a,self.b,self.c))

Add().readval()
Add().readval()