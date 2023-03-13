import tkinter as tk
from tkinter import ttk
import threading
from tkinter import messagebox as m_box
from pytube import YouTube


def on_link():
    try:
        yt = YouTube(link.get())
        video = yt.streams.get_highest_resolution()
        video.download(path.get())
        m_box.showinfo("Success", "Video downloaded")
    except Exception:
        m_box.showerror("Error","Connection Problem! ")

def download_yt_video():
    threading.Thread(target=on_link)


root = tk.Tk()

root.title("Youtube video downloader")
root.geometry("500x400")
root.resizable(0, 0)
root.config()

main_frame = ttk.Frame(root)
main_frame.pack(padx=70, pady=70)

lbl_yt_link = ttk.Label(main_frame, text="Youtube Link: ")
lbl_yt_link.grid(row=0, column=0)

link = tk.StringVar()
txt_yt_link = ttk.Entry(main_frame,width=60, textvariable=link)
txt_yt_link.grid(row=0, column=1)
txt_yt_link.focus()

lbl_to_path = ttk.Label(main_frame, text="Path")
lbl_to_path.grid(row=1, column=0)

path = tk.StringVar()
txt_to_path = ttk.Entry(main_frame, width=60, textvariable=path)
txt_to_path.grid(row=1, column=1)


ttk.Button(main_frame, text="Choose file").grid(row=2, column=0)
ttk.Button(main_frame, text="Download video", command=download_yt_video).grid(row=2, column=1)





""" 
pack
grid
place

 """


root.mainloop()
