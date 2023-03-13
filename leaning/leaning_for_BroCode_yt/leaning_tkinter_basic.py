# tkinter leaning
from tkinter import *
import tkinter as tk

# widgets = GUI elements: buttons, textboxs, labels, images
# window = serves as a container to hold or contain these widgets

window = tk.Tk()    # instantiate an instance of a window
window.geometry("420x420")
window.title("Bro code first GUI program")

#icon = tk.PhotoImage(file="D:\\leaning python\\hello.png")
#window.iconphoto(True, icon)

window.config(background="#5cfcff")

# ------------------------------------------------------------------------
# label = an area widget that holds text and/or image within a window

photo = PhotoImage(file='D:\\leaning python\\hello.png')

label = Label(window, text="Hello World",
                       font=("Arial", 40, "bold"), 
                       fg="#00ff00", 
                       bg='black',
                       relief=RAISED,
                       bd=10,
                       padx=20,
                       pady=20,
                       image=photo)

label.pack()
#label.place(x=100, y=100)



window.mainloop()   # place window on computer screen, listen for events