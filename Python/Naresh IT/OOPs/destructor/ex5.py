# program for demonstrating garbage Collector running Process
import gc

print("Program started")
print("Initially, Is GC Running:",gc.isenabled())   #True
a = 10
b = 20
c = a + b
print(f'Value of a = {a}')
gc.disable()
print(f"Value of b = {b}")
print("Now Is GC Running:",gc.isenabled()) # False
print("sum={}".format(c))
gc.enable()
print("Now Is GC Running:",gc.isenabled()) # True
print("Program Execution Ended")


# if we disable the GC then also internally run using PVM and OS