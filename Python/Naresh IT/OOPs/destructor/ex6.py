# called GC Automatically when Program end
# program for demonstrating garbage Collector running Process
import sys,time,gc
class Employee:
    def __init__(self,eno,ename):
        print("-------------------------------")
        print("Program Started")
        self.eno = eno
        self.ename = ename
        print("-------------------------------")
        print(f'Employee Number: {eno}')
        print(f'Employee Name: {ename}')
        print("--------------------------------")
    def __del__(self):
        print("Garbage collector calls __del__(self) for de-allocation the memory")
        global totsize
        totsize = totsize-sys.getsizeof(self)
        print("Now available memory is ", totsize)

print("Program started")
print("Initially, Is GC Running:",gc.isenabled()) # True
print("-------------------------------------------------------")
gc.disable()
print("Now, Is GC Running after disable:",gc.isenabled()) # False
e1 = Employee(10,"Travis")
e2 = Employee(20,"Russom")
e3 = Employee(30,"Richi")
totsize = sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory space ",totsize)
time.sleep(3)
print("Program ended")
print("Now, Is GC Running after disable:",gc.isenabled()) # False

# here we disable the GC but it is running properly