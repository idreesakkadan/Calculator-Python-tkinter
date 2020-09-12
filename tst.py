from tkinter import *

master = Tk()


def e1_delete():
    e1.delete(first=0, last=100)


e1 = Entry(master, width=35)
e1.grid(row=0, column=0)

b_erase = Button(master, text="Erase", command=e1_delete)
b_erase.grid(row=1, column=0)



master.mainloop()
