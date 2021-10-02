# Program to create a customized digital clock

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def digi_clock():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, digi_clock)

font_des = input("Enter font: ")
background_des = input("Enter background color: ")
foreground_des = input("Enter foreground color: ")
size = int(input("Enter the size: "))

lbl= Label(root, font=(font_des, size), background=background_des, foreground=foreground_des)
lbl.pack(anchor ='center')
digi_clock()

mainloop()
