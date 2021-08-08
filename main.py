from tkinter import *

tkWindow = Tk()
tkWindow.geometry('800x480')
tkWindow.title('PythonExamples.org - Tkinter Example')

postal_code = []
postal_code_var = StringVar()
postal_code_var.set('')
postal_code_label = Label(tkWindow, textvariable=postal_code_var).grid(column=1, row=0)


def selectNumber(number):
    postal_code.append(number)
    postal_code_var.set(postal_code)
    print(number)


def save():
    print(postal_code)


def delete():
    postal_code.pop()
    postal_code_var.set(postal_code)


button_1 = Button(tkWindow, text='1', command=lambda: selectNumber(1)).grid(row=1, column=0)
button_2 = Button(tkWindow, text='2', command=lambda: selectNumber(2)).grid(row=1, column=1)
button_3 = Button(tkWindow, text='3', command=lambda: selectNumber(3)).grid(row=1, column=2)
button_4 = Button(tkWindow, text='4', command=lambda: selectNumber(4)).grid(row=2, column=0)
button_5 = Button(tkWindow, text='5', command=lambda: selectNumber(5)).grid(row=2, column=1)
button_6 = Button(tkWindow, text='6', command=lambda: selectNumber(6)).grid(row=2, column=2)
button_7 = Button(tkWindow, text='7', command=lambda: selectNumber(7)).grid(row=3, column=0)
button_8 = Button(tkWindow, text='8', command=lambda: selectNumber(8)).grid(row=3, column=1)
button_9 = Button(tkWindow, text='9', command=lambda: selectNumber(9)).grid(row=3, column=2)
button_0 = Button(tkWindow, text='0', command=lambda: selectNumber(0)).grid(row=4, column=1)
button_save = Button(tkWindow, text='Speichern', command=lambda: save()).grid(row=4, column=2)
button_delete = Button(tkWindow, text='Löschen', command=lambda: delete()).grid(row=4, column=0)

tkWindow.columnconfigure(0, weight=1)
tkWindow.columnconfigure(1, weight=1)
tkWindow.columnconfigure(2, weight=1)
tkWindow.rowconfigure(1, weight=1)
tkWindow.rowconfigure(2, weight=1)
tkWindow.rowconfigure(3, weight=1)

tkWindow.mainloop()
