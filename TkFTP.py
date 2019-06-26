from tkinter import *

window = Tk()
window.iconbitmap("tk.ico")
window.title("TkFTP")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

Label(window, text="Host").grid(row=0)
Label(window, text="Username").grid(row=1)
Label(window, text="Password").grid(row=2)
Label(window, text="Port").grid(row=3)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window, show="*")
e4 = Entry(window)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

window.mainloop()