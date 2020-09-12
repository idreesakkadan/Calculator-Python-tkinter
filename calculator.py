from tkinter import *

calc = Tk()
calc.geometry("280x240")
calc.title("Idri's Calculator")
calc.configure(background='grey')
display_in = StringVar()
operator = ""


def click_button(number):
    global operator
    operator = operator + str(number)
    display_in.set(operator)


def equal_button():
    global operator
    #print(operator)
    add = str(eval(operator))
    display_in.set(add)
    operator = ''


def clear_button():
    global operator
    display.delete(first=0, last=100)
    operator = ''


def perc_button():
    global operator
    perc =int(operator)/100
    #print(perc)
    display_in.set(perc)
    operator = ''


def button_backspace():
    global operator
    operator = operator[:-1]  # Remove last digit
    if operator:  # If there is at list one digit
        display_in.set(operator)
    else:  # In this case display 0 in text_box
        display_in.set('')


display = Entry(calc, font=("Courier New", 12, 'bold'), width=25, bd=5, bg='grey', textvar=display_in)
display.grid(column=0, row=0, columnspan=6)

# numbers button
b7 = Button(calc, text=7, bg='black', fg='white', command=lambda: click_button(7), font=('Corbel Light', 15, 'bold'))
b7.grid(row=2, column=0, sticky='nesw')

b8 = Button(calc, text=8, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(8))
b8.grid(row=2, column=1, sticky='nesw')

b9 = Button(calc, text=9, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(9))
b9.grid(row=2, column=2, sticky='nesw')

b4 = Button(calc, text=4, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(4))
b4.grid(row=3, column=0, sticky='nesw')

b5 = Button(calc, text=5, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(5))
b5.grid(row=3, column=1, sticky='nesw')

b6 = Button(calc, text=6, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(6))
b6.grid(row=3, column=2, sticky='nesw')

b1 = Button(calc, text=1, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(1))
b1.grid(row=4, column=0, sticky='nesw')

b2 = Button(calc, text=2, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(2))
b2.grid(row=4, column=1, sticky='nesw')

b3 = Button(calc, text=3, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(3))
b3.grid(row=4, column=2, sticky='nesw')

b0 = Button(calc, text=0, bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=lambda: click_button(0))
b0.grid(row=5, column=0, sticky='nesw')

b00 = Button(calc, text='00', bg='black', fg='white', font=('Corbel Light', 15, 'bold'),
             command=lambda: click_button('00'))
b00.grid(row=5, column=1, sticky='nesw')

b11 = Button(calc, text='. ', bg='black', fg='white', font=('Corbel Light', 15, 'bold'),
             command=lambda: click_button('.'))
b11.grid(row=5, column=2, sticky='nesw')

# operators button
button_div = Button(calc, text='÷', bg='black', fg='#11ad31', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('/'))
button_mul = Button(calc, text='x', bg='black', fg='#11ad31', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('*'))
button_min = Button(calc, text='-', bg='black', fg='#11ad31', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('-'))
button_plus = Button(calc, text='+', bg='black', fg='#11ad31', font=('Corbel Light', 15, 'bold'), command=lambda: click_button('+'))
button_perc = Button(calc, text='%', bg='black', fg='white', font=('Corbel Light', 15, 'bold'), command=perc_button)
button_back = Button(calc, text='←', bg='black', fg='#ad4e2b', font=('Corbel Light', 15, 'bold'), command=button_backspace)

button_div.grid(row=1, column=3, sticky="news", columnspan=3)
button_mul.grid(row=2, column=3, sticky="news", columnspan=3)
button_min.grid(row=3, column=3, sticky="news", columnspan=3)
button_plus.grid(row=4, column=3, sticky="news", columnspan=3)
button_perc.grid(row=1, column=1, sticky="news")
button_back.grid(row=1, column=2, sticky="news")

button_clr = Button(calc, text='C', bg='black', fg='#bf3908', font=('Corbel Light', 15, 'bold'), command=clear_button)
button_clr.grid(row=1, column=0, sticky="news")

button_equ = Button(calc, text='=', bg='black', fg='#11ad31', font=('Corbel Light', 15, 'bold'), command=equal_button)
button_equ.grid(row=5, column=3, sticky="news", columnspan=3)

calc.mainloop()
