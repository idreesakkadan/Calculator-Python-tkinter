import tkinter as tk


root = tk.Tk()
my_string_var = tk.StringVar()
my_string_var.set('First Time')
tk.Label(root, textvariable=my_string_var).grid()
root.mainloop()