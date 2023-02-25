from tkinter import *
from tkinter import messagebox
import random

##root = Tk()
##root.geometry("300x200")

rand = random.randint(200, 500)
for x in range(rand):
    messagebox.askretrycancel("askretrycancel", "Try again?")
    
##messagebox.showinfo("showinfo", "Information")

##messagebox.showerorr("showwarning", "Warning")

##messagebox.askquestion("askquestion", "Are you sure?")

##messagebox.askokcancel("askokcancel", "Want to continue?")

##messagebox.askyesno("askyesno", "Find the value?")


##messagebox.showwarning("Warning", "This is an Error")

##root.mainloop()
