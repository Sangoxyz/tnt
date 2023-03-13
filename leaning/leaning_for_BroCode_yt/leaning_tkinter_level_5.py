# radio button = similar to checkbox, but yor can only select one from a group

from tkinter import *

food = ["pizza", "humberger", "hotdog"]

def order():
    if(x.get()==0):
        print("You order Pizza")
    elif(x.get()==1):
        print("You order humberger")
    else:
        print("You order hotdog")

""" pizzaImage = PhotoImage(file='hello.png')
hamburgerImage = PhotoImage(file='hello.png')
hotdogImage = PhotoImage(file='hello.png')
foodImage = [pizzaImage, hamburgerImage, hotdogImage] """

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                                text=food[index],   # add text to radio buttons
                                variable=x,     # groups radiobuttons together if they share
                                value=index,    # assigns each radiobutton a different value
                                padx=25,        # adds padding on x-axis
                                font=("Impact",50),
                                #image= foodImage[index],
                                compound='left',
                            
                                indicatoron=0,
                                width=75,
                                command=order
                                )    


    
    
    
    radiobutton.pack(anchor=W)





window.mainloop()