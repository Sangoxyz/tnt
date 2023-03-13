import sys
import os
import tkinter as tk
from datetime import datetime
import time


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = tk.Tk()

root.title("Digital Clock")
root.geometry("200x100")
root.config(bg='black')
root.iconbitmap(default = resource_path("clock-f.ico"))
root.resizable(0, 0) # khong thay doi gia tri cua khung

lbl_time = tk.Label(root, font=('Segoe UI', 18,"bold"), bg='black', fg='blue')




def update_time():
    weekday = [f"Thứ {x}" for x in range (2, 8)] + ["Chủ nhật"]
    wd_num = datetime.now().weekday()


    current_time = time.strftime("%H:%M:%S\n%d-%m-%Y") + f"\n{weekday[wd_num]}"
    lbl_time.config(text=current_time)
    lbl_time.after(80, update_time)


lbl_time.pack(anchor="center")
update_time()



root.mainloop()