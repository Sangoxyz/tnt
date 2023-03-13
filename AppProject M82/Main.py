import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, Menu, Text, Toplevel, Scrollbar
from tkinter import font
import sys
from tkinter.constants import E, S
import M82app
from M82app import *
from M82app import M82file
from M82app import Taode
import regex as re
from tkinter import filedialog as fd
import tkinter.messagebox as mbox
from tkinter.messagebox import showinfo
checkMN = 0

LARGEFONT = ("Verdana", 20)
Normalfont = ("Verdana", 10, font.BOLD)
Smallfont = ("Verdana", 10)
kitu = ["?/~", "⸍", "⸌", ".", "_"]
M82_color = [['sky blue', 'sky blue', 'sky blue', 'sky blue', 'sky blue'],
             ['sky blue', 'light salmon', 'light salmon',
                 'light salmon', 'light salmon'],
             ['sky blue', 'light salmon', 'seashell3', 'seashell3', 'seashell3'],
             ['sky blue', 'light salmon', 'seashell3',
                 'spring green', 'spring green'],
             ['sky blue', 'light salmon', 'seashell3',
                 'spring green', 'medium orchid'],
             ]


def Taodetool(win):
    newWin = Toplevel(win)
    newWin.geometry('700x680+600+0')
    newWin.resizable(False, False)
    newWin.title('Tạo đề')
    openbut = Button(newWin, text='Mở tệp', command=lambda: select_file())
    openbut.place(x=0, y=5)
    lbl1 = tk.Label(newWin, text='ĐIỆN MÃ:', font=Normalfont)
    lbl1.place(x=0, y=32)
    txtb1 = tk.Text(newWin, height=19, width=74, font=Smallfont)
    txtb1.place(x=100, y=35)
    lbl2 = tk.Label(newWin, text='ĐIỆN DỊCH:', font=Normalfont, bg='azure')
    lbl2.place(x=0, y=367)
    txtb2 = tk.Text(newWin, height=19, width=74, font=Smallfont, bg='dim gray')
    txtb2.place(x=100, y=370)
    # newWin.bind('<Motion>', motion)
    Button1 = tk.Button(newWin, text='Tạo đề', width=5,
                        command=lambda: Taodemain())
    Button1.place(x=60, y=5)
    Button2 = tk.Button(newWin, text='In đề', width=5)
    Button2.place(x=120, y=5)
    lblde = Label(newWin, text='Đề số:', font=Smallfont)
    lblde.place(x=400, y=5)
    Ent = Entry(newWin, width=6, font=Smallfont)
    Ent.insert(0, '0')
    Ent.place(x=450, y=5)

    def Taodemain():
        text1 = txtb1.get("1.0", "end-1c")
        text2 = txtb2.get("1.0", "end-1c")
        denum = Ent.get()
        if Taode.Taode(text1, text2, denum) == True:
            mbox.showerror('Lỗi', 'Tệp cũ chưa tắt, không thể tạo tệp mới!')
        else:
            mbox.showinfo(
                'Thành công', 'Tạo đề xong, kiểm tra trong folder chứa đề!')

    def select_file():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*'))
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        f = open(filename, encoding='utf-8')
        alltext = ''.join(f.readlines())
        text1, text2 = Taode.Laydulieu(alltext)
        txtb1.insert('1.0', text1)
        txtb2.insert('1.0', text2)


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Mật ngữ App")
        menubar = Menu(container)
        self.config(menu=menubar)
        menufile = Menu(menubar)
        menufile.add_command(label="Đóng")
        menubar.add_cascade(label="Tùy chọn", menu=menufile)
        menufile2 = Menu(menubar)
        # menufile2.add_command(label = "Mật ngữ M82", command=lambda: self.show_frame(M82page))
        menufile2.add_command(label="Mật ngữ M82",
                              command=lambda: self.show_frame(M82page, 0))
        menufile2.add_command(label="Mật ngữ PBC",
                              command=lambda: self.show_frame(M82page, 1))
        menubar.add_cascade(label="Chọn mật ngữ", menu=menufile2)
        menufile3 = Menu(menubar)
        menufile3.add_command(
            label="M82", command=lambda: self.show_frame(M82changePage, checkMN))
        menufile3.add_command(label="PBC")
        menubar.add_cascade(label="Sửa vành khóa", menu=menufile3)

        menufile4 = Menu(menubar)
        menufile4.add_command(label="Tạo đề", command=lambda: Taodetool(self))
        menubar.add_cascade(label="Công cụ", menu=menufile4)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (M82changePage, M82page):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(M82page, 0)
    # to display the current frame passed as
    # parameter

    def show_frame(self, cont, intck):
        M82page = self.get_page('M82page')
        global checkMN
        if intck == 1:
            M82page.label.configure(text='Mật ngữ PBC')
            checkMN = 1
        else:
            M82page.label.configure(text='Mật ngữ M82')
            checkMN = 0
        print(checkMN)
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_name):
        for page in self.frames.values():
            if str(page.__class__.__name__) == page_name:
                return page
        return None
# first window frame startpage


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


class M82changePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        entKtren = []
        entKtren2 = []
        entKduoi = []
        entKduoi2 = []
        global checkMN
        frameX = tk.Frame(self)
        for i in range(31):
            for j in range(15):
                if j <= 4:
                    if i <= 4:
                        labelDau = tk.Label(
                            frameX, width=4, font=Normalfont, justify=tk.CENTER, bg=M82_color[i][j], relief=tk.SUNKEN)
                        if i == j:
                            labelDau.configure(text=kitu[i])
                        labelDau.grid(column=j, row=i, padx=0, pady=0)
                        # entry.configure(state= "disabled")
                    elif i > 4 and i <= 10:
                        entry = tk.Entry(
                            frameX, width=4, font=Smallfont, justify=tk.CENTER, bg=M82_color[j][j])
                        entry.grid(column=j, row=i, padx=0, pady=0)
                        entry.configure(font=Normalfont)
                        entry.insert(1, M82file.M82numPA[i-5][j])
                        entKtren.append(entry)
                    else:
                        labelDau = tk.Label(frameX, width=4, font=Normalfont, justify=tk.CENTER,
                                            bg=M82_color[j][j], relief=tk.GROOVE, text=M82file.M82numNA[i-11][j])
                        labelDau.grid(column=j, row=i, padx=0, pady=0)
                else:
                    if i <= 4:
                        entry = tk.Entry(
                            frameX, width=7, font=Smallfont, justify=tk.CENTER, bg=M82_color[i][i])
                        entry.configure(font=Normalfont)
                        entry.insert(1, M82file.M82dau[i][j-5])
                        entry.grid(column=j, row=i, padx=0, pady=0)
                        entKduoi.append(entry)
                    elif i > 4 and i <= 10:
                        if M82file.M82charPA[i-5][j-5] == ' ' or M82file.M82charNA[i-11][j-5] == '  ':
                            labelDauchar = tk.Label(frameX, width=8, text=M82file.M82charPA[i-5][j-5].capitalize(
                            ), font=Smallfont, justify=tk.CENTER, bg='snow4', relief=tk.GROOVE)
                        else:
                            labelDauchar = tk.Label(frameX, width=8, text=M82file.M82charPA[i-5][j-5].capitalize(
                            ), font=Smallfont, justify=tk.CENTER, bg='khaki3', relief=tk.GROOVE)
                        labelDauchar.grid(column=j, row=i, padx=0, pady=0)
                    else:
                        if M82file.M82charNA[i-11][j-5] == ' ' or M82file.M82charNA[i-11][j-5] == '  ':
                            labelDauchar = tk.Label(
                                frameX, width=8, text=M82file.M82charNA[i-11][j-5], font=Smallfont, justify=tk.CENTER, bg='snow4', relief=tk.GROOVE)
                        else:
                            labelDauchar = tk.Label(
                                frameX, width=8, text=M82file.M82charNA[i-11][j-5], font=Smallfont, justify=tk.CENTER, bg='khaki', relief=tk.GROOVE)
                        labelDauchar.grid(column=j, row=i, padx=0, pady=0)
            entKtren2.append(entKtren)
            entKduoi2.append(entKduoi)
        frameX.pack(side=tk.LEFT, anchor=tk.NW)
        frameY = tk.Frame(self, background="blue")
        butt = tk.Button(frameY, text="Lưu")
        butt.pack(pady=5, padx=1)
        print(checkMN)
        butt2 = tk.Button(
            frameY, text="Hủy", command=lambda: controller.show_frame(M82page, checkMN))
        butt2.pack(pady=5, padx=1)
        frameY.pack(side=tk.LEFT, pady=0, padx=10, anchor=tk.NW)
# second window frame page1


class M82page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Frame 1: Ten page
        frame1 = tk.Frame(self, width=900, height=40, bg='yellow')
        frame1.place(x=0, y=0)
        self.label = tk.Label(frame1, text="Mật ngữ M82", font=LARGEFONT)
        self.label.place(x=365, y=0)
        # --------------------------

        # Frame 2: Cac button chuc nang
        frame2 = tk.Frame(self, width=900, height=640, bg='pink')
        frame2.place(x=900, y=0)
        Voicebutt = tk.Button(frame2, text='Voice', width=10)
        Voicebutt.place(x=5, y=40)
        Taodebutt = tk.Button(frame2, text='Tạo đề', width=10)
        Taodebutt.place(x=5, y=75)
        Copybutt = tk.Button(frame2, text='Sao chép', width=10)
        Copybutt.place(x=5, y=335)
        Printbutt = tk.Button(frame2, text='In đáp án', width=10)
        Printbutt.place(x=5, y=370)
        # -------------------
        # Frame 3: TXT box
        frame3 = tk.Frame(self, width=900, height=295, bg='red')
        frame3.place(x=0, y=40)
        Txt1 = Text(master=frame3, height=18, width=113,
                    font=Smallfont, wrap='word')
        Txt1.place(x=0, y=0)
        sb1 = Scrollbar(frame3)
        sb1.place(x=885, y=0, relheight=1)

        Txt1.config(yscrollcommand=sb1.set)
        sb1.config(command=Txt1.yview)

        # -------------
        # Frame 4: button mã và giải mã
        frame4 = tk.Frame(self, width=900, height=30, bg='blue')
        frame4.place(x=0, y=335)
        Codebutt = tk.Button(frame4, text="Mã điện", width=10,
                             height=1, font=Normalfont, command=lambda: Madichdien(0))
        Codebutt.place(x=350, y=0)
        DecodeButt = tk.Button(frame4, text="Dịch điện", width=10,
                               height=1, font=Normalfont, command=lambda: Madichdien(1))
        DecodeButt.place(x=455, y=0)
        # -------------
        # Frame 5: TXT đáp án
        frame5 = tk.Frame(self, width=900, height=290, bg='dark gray')
        frame5.place(x=0, y=365)
        Txt2 = Text(master=frame5, height=17, width=113, font=Smallfont)
        Txt2.place(x=0, y=0)
        Txt2.config(state='disable')
        sb2 = Scrollbar(frame5)
        sb2.place(x=885, y=0, relheight=1)

        Txt2.config(yscrollcommand=sb2.set)
        sb2.config(command=Txt2.yview)

        def Madichdien(int):
            global checkMN
            txt = Txt1.get("1.0", "end-1c")
            listTxt = re.split(f'\n', txt)
            Txt2.configure(state='normal')
            Txt2.delete("1.0", "end-1c")
            text = ''
            if checkMN == 0:
                for i in range(len(listTxt)):
                    if int == 0:
                        text = text + M82file.Encodesent(listTxt[i]) + '\n'
                    else:
                        text = text + M82file.DecodeNs(listTxt[i]) + '\n'
            else:
                print('alo')
            Txt2.insert(1.0, text)
            Txt2.config(state='disable')
# third window frame page2


if __name__ == '__main__':
    app = tkinterApp()
    window_width = 1000
    window_height = 680
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    tk.CENTER_x = int(screen_width/2 - window_width / 2)
    tk.CENTER_y = int(screen_height/2 - window_height / 2) - 47
    app.geometry(f'{window_width}x{window_height}+{tk.CENTER_x}+{tk.CENTER_y}')
    app.resizable(False, False)
    # app.bind('<Motion>', motion)

    app.mainloop()
