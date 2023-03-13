# file save

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="D:\\leaning python",        # duong dan
                                    defaultextension='.txt',                # luu mac dinh
                                    filetype=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All file",".*"),                  # cac loai file lua chon
                                    ])

    if file is None:
        return
    #filetext = str(text.get(1.0, END))
    filetext = input("Enter some text I guess: ")

    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()


window.mainloop()
