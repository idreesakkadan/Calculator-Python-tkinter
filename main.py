from tkinter import *


calc = Tk()
calc.geometry("350x350")
calc.title("Calculator")
calc.configure(background='grey')
display_in = StringVar()
operator = ""





def click_button(number):
    global operator
    operator = operator + str(number)
    display_in.set(operator)


def equal_button():
    global operator
    add = str(eval(operator))
    display_in.set(add)
    operator = ''

def clear_button():
    display_in.set('')



display = Entry(calc,font=("Courier New",12,'bold'),width=25,bd=5,bg='grey',textvar=display_in)
display.grid(column=0, row=0, columnspan=6)

# numbers button
b1 = Button(calc, text=7, bg='black', fg='white', command=lambda: click_button(7), font=('Corbel Light', 15, 'bold'))
b2 = Button(calc, text=8, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(8))
b3 = Button(calc, text=9, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(9))
b4 = Button(calc, text=4, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(4))
b5 = Button(calc, text=5, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(5))
b6 = Button(calc, text=6, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(6))
b7 = Button(calc, text=1, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(1))
b8 = Button(calc, text=2, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(2))
b9 = Button(calc, text=3, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(3))
b10 = Button(calc, text=0, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(0))
b11 = Button(calc, text='. ', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('.'))

# operators button
bo1 = Button(calc, text='÷', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('/'))
bo2 = Button(calc, text='←', bg='black', fg='white', font=('Corbel Light', 15, 'bold'))
bo4 = Button(calc, text='x', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('*'))
bo5 = Button(calc, text='( ', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('('))
bo6 = Button(calc, text=') ', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(')'))
bo7 = Button(calc, text='- ', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('-'))
bo8 = Button(calc, text='x²', bg='black', fg='white', font=('Corbel Light', 15, 'bold'))
bo9 = Button(calc, text='√', bg='black', fg='white', font=('Corbel Light', 15, 'bold'))
bo10 = Button(calc, text='00', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(00))
bo11 = Button(calc, text='+', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('+'))
bo12 = Button(calc, text='=', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=equal_button)

# row1
b1.grid(row=1, column=0, sticky='nesw')
b2.grid(row=1, column=1, sticky='nesw')
b3.grid(row=1, column=2, sticky='nesw')
bo1.grid(row=1, column=3, sticky='nesw')
bo2.grid(row=1, column=4, sticky='nesw', columnspan=2)


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
