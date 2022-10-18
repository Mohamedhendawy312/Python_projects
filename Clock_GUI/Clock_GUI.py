from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Live Clock")

def time():
    formate_time = strftime('%H:%M:%S: %p')
    label.config(text=formate_time)
    label.after(1000, time)

label = Label(window , font=("ds-digital", 175), background="black", foreground="white")
label.pack(anchor='center')

time()
mainloop()