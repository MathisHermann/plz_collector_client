import tkFont

from tkinter import *
import datetime

tkWindow = Tk()
tkWindow.geometry('800x480')
tkWindow.title('PythonExamples.org - Tkinter Example')
# tkWindow.configure(bg='black')

font_bold = tkFont.Font(family="Arial", size=50, weight="bold")
font = tkFont.Font(family="Arial", size=50)

postal_code = []
postal_code_var = StringVar()
postal_code_var.set('')
postal_code_label = Label(tkWindow, textvariable=postal_code_var, font=font_bold).grid(row=0, column=0, columnspan=3)


def selectNumber(number):
    if len(postal_code) < 8:
        postal_code.append(number)
        set_text_on_label()


def get_text():
    text = ''
    for char in postal_code:
        text += str(char)
    return text


def save():
    if len(postal_code) > 0:
        f = open("test.csv", "a")
        f.write(get_text() + ',' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '\n')
        f.close()
        del postal_code[:]
        set_text_on_label()


def set_text_on_label():
        postal_code_var.set(get_text())


def delete():
    if len(postal_code) > 0:
        postal_code.pop()
        set_text_on_label()


button_1 = Button(tkWindow, text='1', command=lambda: selectNumber(1)).grid(row=1, column=0, sticky='nsew')
button_2 = Button(tkWindow, text='2', command=lambda: selectNumber(2)).grid(row=1, column=1, sticky='nsew')
button_3 = Button(tkWindow, text='3', command=lambda: selectNumber(3)).grid(row=1, column=2, sticky='nsew')
button_4 = Button(tkWindow, text='4', command=lambda: selectNumber(4)).grid(row=2, column=0, sticky='nsew')
button_5 = Button(tkWindow, text='5', command=lambda: selectNumber(5)).grid(row=2, column=1, sticky='nsew')
button_6 = Button(tkWindow, text='6', command=lambda: selectNumber(6)).grid(row=2, column=2, sticky='nsew')
button_7 = Button(tkWindow, text='7', command=lambda: selectNumber(7)).grid(row=3, column=0, sticky='nsew')
button_8 = Button(tkWindow, text='8', command=lambda: selectNumber(8)).grid(row=3, column=1, sticky='nsew')
button_9 = Button(tkWindow, text='9', command=lambda: selectNumber(9)).grid(row=3, column=2, sticky='nsew')
button_0 = Button(tkWindow, text='0', command=lambda: selectNumber(0)).grid(row=4, column=1, sticky='nsew')
button_save = Button(tkWindow, text='Speichern', command=lambda: save()).grid(row=4, column=2, sticky='nsew')
button_delete = Button(tkWindow, text='Loeschen', command=lambda: delete()).grid(row=4, column=0, sticky='nsew')

tkWindow.columnconfigure(0, weight=1)
tkWindow.columnconfigure(1, weight=1)
tkWindow.columnconfigure(2, weight=1)
tkWindow.rowconfigure(0, weight=1)
tkWindow.rowconfigure(1, weight=1)
tkWindow.rowconfigure(2, weight=1)
tkWindow.rowconfigure(3, weight=1)

tkWindow.mainloop()
