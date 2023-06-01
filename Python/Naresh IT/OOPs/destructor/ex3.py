# called GC forcefully using DEL Keyeword
import sys,time
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
print("Employee e1 no longer to access... Forcefully called garbage collector")
del e1   # Garbage Collector calls Destructor  forcefully--Forceful Garbage Collection
time.sleep(1)
e2 = Employee(20,"Russom")
print("Employee e2 no longer to access... Forcefully called garbage collector")
del e2   # Garbage Collector calls Destructor  forcefully--Forceful Garbage Collection
time.sleep(1)
e3 = Employee(30,"Richi")
print("Employee e2 no longer to access... Forcefully called garbage collector")
del e3   # Garbage Collector calls Destructor  forcefully--Forceful Garbage Collection
time.sleep(1)

print("Program ended")