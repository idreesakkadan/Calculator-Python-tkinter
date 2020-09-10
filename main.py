from tkinter import *

calc = Tk()
calc.geometry("400x400")
calc.title("Calculator")
calc.configure(background='grey')

b1 = Button(calc, text=7, bg='black', fg='white')
b2 = Button(calc, text=8, bg='black', fg='white')
b3 = Button(calc, text=9, bg='black', fg='white')
b4 = Button(calc, text=4, bg='black', fg='white')
b5 = Button(calc, text=5, bg='black', fg='white')
b6 = Button(calc, text=6, bg='black', fg='white')
b7 = Button(calc, text=1, bg='black', fg='white')
b8 = Button(calc, text=2, bg='black', fg='white')
b9 = Button(calc, text=3, bg='black', fg='white')
b10 = Button(calc, text=0, bg='black', fg='white')

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
bo1.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b10.grid(row=3, column=0)
# b.grid(row=3, column=1)


calc.mainloop()
