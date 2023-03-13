import tkinter as tk
import time


root = tk.Tk()
root.title("Digital clock")
root.geometry("500x100")


# def time

def next_time():
	current_time = time.strftime("%H:%M:%S: %p")
	lbl_time.config(text=current_time)
	lbl_time.after(1000, next_time)

# lable
lbl_time = tk.Label(root, font=("ds-digital", 50), bg="black", fg="blue")
lbl_time.pack(anchor=tk.CENTER)
next_time()








root.mainloop()