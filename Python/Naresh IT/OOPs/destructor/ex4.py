# GC check When DEEP copy held on the program
import time
class Employee:
    def __init__(self,eno,ename):
        print("--------------------------------")
        print("Program Started")
        self.eno = eno
        self.ename = ename
        print("-------------------------------")
        print(f'Employee Number: {eno}')
        print(f'Employee Name: {ename}')
        print("--------------------------------")
    def __del__(self):
        print("Garbage collector calls __del__(self) for de-allocation the memory")

print("Program started")
e1 = Employee(10,"Travis")
e2 = e1 #Deep copy
e3 = e1 #Deep copy

print(e1.__dict__, id(e1))
print(e2.__dict__, id(e2))
print(e3.__dict__, id(e3))

time.sleep(2)
print("Program ended")