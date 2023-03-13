import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()


root.iconbitmap("Minion-Hello.ico")
root.title("Hello GUI World")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg = "#264653")

def make_lable():
	first_name = name_entry.get()

	if case_stye.get() == "nomal":
		name_lable = tk.Label(output_frame, text = "Hello" + first_name + "!", bg = "#219ebc", fg = "white" )
	elif case_stye.get() == "upper":
		name_lable = tk.Label(output_frame, text = ("Hello" + first_name + "!").upper(), bg = "#219ebc", fg = "white" )
	name_lable.pack(pady = 5)
	name_entry.delete(0, tk.END) # delete nhung gi da nhap


input_frame = tk.Frame(root, bg = "#8ecae6")
output_frame = tk.Frame(root, bg = "#219ebc")

input_frame.pack()
output_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)



case_stye = tk.StringVar()
case_stye.set("nomal")

# name and button
name = tk.StringVar()
name_entry = tk.Entry(input_frame, width = 20)
submit_button = tk.Button(input_frame, text = "Submit", command = make_lable)

# radio section
normal_radio = tk.Radiobutton(input_frame, text = "Normal Case", variable = case_stye, value = "nomal", bg = "#8ecae6")
upper_radio = tk.Radiobutton(input_frame, text = "Upper Case", variable = case_stye, value = "upper", bg = "#8ecae6")

# insert image
smile_img = ImageTk.PhotoImage(Image.open("smile.png"))
smile_label = tk.Label(output_frame, image = smile_img, bg = "#219ebc" )
smile_label.pack()






name_entry.grid(row = 0, column = 0, padx = 10, pady = (10, 0))
submit_button.grid(row = 0, column = 1, padx = 10, pady = (10, 0), ipadx = 30)
normal_radio.grid(row = 1, column = 0, padx = 10, pady = 10)
upper_radio.grid(row = 1, column = 1, padx = 10, pady = 10)





root.mainloop()