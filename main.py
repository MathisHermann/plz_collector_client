"""
main.py
This is the client application for a plz collection system to allow the collection of postal-codes.
This application can run in every environment that supports python3 and is developed explicitly to run on a Raspberry Pi.
"""

import tkinter.font as tkfont
from tkinter import *
from cryptography.fernet import Fernet
from urllib import request, parse
import datetime
import json
import requests
import socket
import threading

safe_on_remote_server = True

data_target_url = 'http://plz.bitwi.ch/api/postal-codes'
ENCRYPTION_KEY = b'Encryption key goes here'

temp_file_name = "temp_plz.csv"
perm_file_name = "perm_plz.csv"

tkWindow = Tk()
tkWindow.geometry('800x480')
tkWindow.title('PythonExamples.org - Tkinter Example')
# tkWindow.configure(bg='black')

font_bold = tkfont.Font(family="Arial", size=50, weight="bold")
font = tkfont.Font(family="Arial", size=50)

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
        date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        temp_file = open(temp_file_name, "a")
        text_to_file = date_time + ';' + get_text()
        temp_file.write(text_to_file + '\n')
        temp_file.close()
        del postal_code[:]
        set_text_on_label()
        num_lines = sum(1 for line in open(temp_file_name))
        if safe_on_remote_server and internet() and num_lines >= 10:
            send_thread = threading.Thread(target=send_data)
            send_thread.start()


def set_text_on_label():
    postal_code_var.set(get_text())


def delete():
    if len(postal_code) > 0:
        postal_code.pop()
        set_text_on_label()


def send_data():
    perm_file = open(perm_file_name, "a")
    temp_file = open(temp_file_name, "r")
    counter = 0
    send_codes = []
    line = temp_file.readline()
    while len(line) > 0:
        counter += 1
        perm_file.write(line)
        send_codes.append(entangle(line))
        line = temp_file.readline()
    perm_file.close()
    temp_file.close()
    server_response = post_data(send_codes)
    if str(server_response) == '200':
        open(temp_file_name, 'w').close()


def entangle(line):
    line = line.strip('\n')
    line_parts = line.split(';')
    return '"' + line_parts[0] + '":{ "plz":' + line_parts[1] + ', "date_time": "' + line_parts[0] + '"}'


def post_data(send_codes):
    message = '{'
    i = 0
    for code in send_codes:
        message += code
        if i != len(send_codes) - 1:
            message += ','
        i += 1
    message += '}'
    token = encrypt_data(message)
    data = {
        "token": token,
    }
    data = json.dumps(data)
    resp = requests.post(data_target_url, json=data)
    return resp.status_code


def encrypt_data(message):
    f = Fernet(ENCRYPTION_KEY)
    token = f.encrypt(message.encode())
    token = str(token)
    token = token[2:len(token) - 1]
    return token

def internet(host="8.8.8.8", port=53, timeout=5):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False


def configure_tkWindow():
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
    tkWindow.rowconfigure(4, weight=1)

if __name__ == '__main__':
    configure_tkWindow()
    tkWindow.mainloop()
