# entry widget = textbox that accepts a singer line of user input

import tkinter as tk

def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state='disabled')

def delete():
    entry.delete(0,last='end')

def backspace():
    entry.delete(len(entry.get())-1, last='end')


window = tk.Tk()

entry = tk.Entry(window,
                 font=("Arial", 50),
                 fg='#00FF00',
                 bg='black',
                 show='*')

#entry.insert(0, 'okok')

entry.pack(side="left")

submit_button = tk.Button(window, text='submit', command= submit)
submit_button.pack(side="right")

delete_button = tk.Button(window, text='delete', command= delete)
delete_button.pack(side="right")

backspace_button = tk.Button(window, text='backspace', command= backspace)
backspace_button.pack(side="right")

window.mainloop()
