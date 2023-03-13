import os
import sys
import tkinter as tk
import threading
from pytube import YouTube
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog


def resource_path(file):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, file)

root = tk.Tk()
root.title("Youtube Video Downloader")
root.iconbitmap(default = resource_path("ytb.ico"))
root.geometry("400x400")
root.resizable(0, 0)




def on_click():
    try:
        yt = YouTube(link.get())
        video = yt.streams.get_highest_resolution()
        video.download(path.get())
        os.startfile(path.get())
        messagebox.showinfo("Success", "Video downloaded!")
        
    except Exception:
        messagebox.showerror("Error", "Connection Problem!")

def get_file_path():
    to_path = filedialog.askdirectory()
    path.set(to_path)


def download_video():
    threading.Thread(target=on_click,)

main_frame = tk.LabelFrame(root, width=400, height=100)
main_frame.pack(padx=10, pady=70) # frame, pad x y set lề
main_frame.pack_propagate(False)

ytb_lable = tk.Label(main_frame, text="Youtube Link: ", bg="#264653",fg="white")
ytb_lable.grid(row=0, column=0, padx=10, pady=10)

link = tk.StringVar()
ytb_entry = tk.Entry(main_frame, width=40, textvariable=link)
ytb_entry.grid(row=0, column=1, padx=10, pady=10)
ytb_entry.focus()

path_label = tk.Label(main_frame, text="Dest", bg="#264653", fg="white")
path_label.grid(row=1, column=0)

extra_frame = tk.Frame(main_frame)
extra_frame.grid(row=1, column=1,sticky="W", padx= (10, 0))

path = tk.StringVar()
path_entry = ttk.Entry(extra_frame, width=25, textvariable=path)
path_entry.config(state="readonly")
path_entry.grid(row=0, column=0)

choose_flie = ttk.Button(extra_frame, text="Choose file", command=get_file_path)
choose_flie.grid(row=0, column=1)

download_btn = ttk.Button(main_frame, text="Download Video", command=download_video)
download_btn.grid(row=2, column=0, columnspan=2,pady=(5, 0))









root.mainloop()