from tkinter import *

calc = Tk()
calc.geometry("400x400")
calc.title("Calculator")
calc.configure(background='grey')

disp = Entry(calc, state='readonly', readonlybackground="grey", width=20)
disp.grid(column=0, row=0, columnspan=6)

# numbers button
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
b11 = Button(calc, text='. ', bg='black', fg='white')

# operators button
bo1 = Button(calc, text='÷', bg='black', fg='white')
bo2 = Button(calc, text='←', bg='black', fg='white')
bo3 = Button(calc, text='C', bg='black', fg='white')
bo4 = Button(calc, text='x', bg='black', fg='white')
bo5 = Button(calc, text='( ', bg='black', fg='white')
bo6 = Button(calc, text=') ', bg='black', fg='white')
bo7 = Button(calc, text='- ', bg='black', fg='white')
bo8 = Button(calc, text='x ', bg='black', fg='white')
bo9 = Button(calc, text='√', bg='black', fg='white')
bo10 = Button(calc, text='%', bg='black', fg='white')
bo11 = Button(calc, text='+', bg='black', fg='white')
bo12 = Button(calc, text='=', bg='black', fg='white')

# row1
b1.grid(row=1, column=0, sticky='nesw')
b2.grid(row=1, column=1, sticky='nesw')
b3.grid(row=1, column=2, sticky='nesw')
bo1.grid(row=1, column=3, sticky='nesw')
bo2.grid(row=1, column=4, sticky='nesw')
bo3.grid(row=1, column=5, sticky='nesw')

# row2
b4.grid(row=2, column=0, sticky='nesw')
b5.grid(row=2, column=1, sticky='nesw')
b6.grid(row=2, column=2, sticky='nesw')
bo4.grid(row=2, column=3, sticky='nesw')
bo5.grid(row=2, column=4, sticky='nesw')
bo6.grid(row=2, column=5, sticky='nesw')

# row3
b7.grid(row=3, column=0, sticky='nesw')
b8.grid(row=3, column=1, sticky='nesw')
b9.grid(row=3, column=2, sticky='nesw')
bo7.grid(row=3, column=3, sticky='nesw')
bo8.grid(row=3, column=4, sticky='nesw')
bo9.grid(row=3, column=5, sticky='nesw')

# row4
b10.grid(row=4, column=0, sticky='nesw')
b11.grid(row=4, column=1, sticky='nesw')
bo10.grid(row=4, column=2, sticky='nesw')
bo11.grid(row=4, column=3, sticky='nesw')
bo12.grid(row=4, column=4, sticky='nesw', columnspan=2)

calc.mainloop()
