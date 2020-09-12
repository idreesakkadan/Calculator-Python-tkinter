from tkinter import *
import math

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.widget()


    def widget(self):
        self.ori = Label(self, text="Enter the desired number:")
        self.ori.grid(row = 1, column = 0, columnspan = 2, sticky =W)

        self.ori2 = Label(self, text="Enter the desired percentage: ")
        self.ori2.grid(row=2, column=0, columnspan = 2, sticky =W)

        self.num = Entry()
        self.num.grid(row=1, column=2, sticky=E)

        self.num1 = Entry()
        self.num1.grid(row = 2, column=2, sticky=E)

        self.label = Label(self, text="The percentage of the selected number is: ")
        self.label.grid(row=3, column=0, columnspan=2, sticky=W)

        btstart = Button(self, text="Calculate", width=7, command=self.cal)
        btstart.grid(row=5, column=0)

        btstop = Button(self, text="exit", width=7, command=self.close_window)
        btstop.grid(row=5, column=1)


    def cal(self):
        self.calc = float(self.num.get()) * float(self.num1.get()) / 100
        print(self.calc)


    def close_window(self):
        root.destroy()



root = Tk()

root.title("Programa de calculo")

app = Application(root)

root.mainloop()