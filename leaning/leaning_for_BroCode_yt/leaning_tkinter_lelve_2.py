# tkinter_levle_2

import tkinter as tk

# button = you click it, then it does stuff
count = 0

def click():
    global count
    count += 1
    print(count)
    #print("You clicked the button!")
    

window = tk.Tk()

#photo = tk.PhotoImage(file='D:\\leaning python\\hello.png')

button = tk.Button(window,
                    text='click me!',
                    command=click,
                    font=('Comic Sans', 30),
                    fg='#00FF00',
                    bg='black',
                    activeforeground='#00FF00',
                    activebackground='black',)
                    #state=ACTIVE,
                    #image=photo,
                    #compound='top')
button.pack()


window.mainloop()