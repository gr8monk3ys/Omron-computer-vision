import tkinter as tk
import tkinter.font as font
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Automation of Visual Inspection")

myFont = font.Font(family='Helvetica')

window.geometry("512x512")

for i in range(13):
    window.grid_columnconfigure(i, weight=2)

for i in range(13):
    window.grid_rowconfigure(i, weight=1)


#black screen image import
image1 = Image.open("blackscreen.jpeg")
resizephoto = image1.resize((150, 150))
photo = ImageTk.PhotoImage(resizephoto)

label1 = tk.Label(window, image=photo)
label1.image = photo
# Position image
# label1.place(x=320, y=100)
label1.grid(column=10, row=2)

#white screen image import
image2 = Image.open("greyscreen.jpeg")
resizephoto = image2.resize((200,20))
photo2 = ImageTk.PhotoImage(resizephoto)
label2 = tk.Label(window, image=photo2)
label2.image = photo2
label2.grid(column=11, row=5)


def clicked1():

    takepic_text.configure(text="Took picture")

def clicked2():

    classify_text.configure(text="Bad/Good")

def clicked3():

    export_text.configure(text="Exporting file/pictures")

#---------
takepic_text = tk.Label(window, width=20, height=5, font=myFont)
takepic_text.grid(column=6, row=1)

classify_text = tk.Label(window, width=20, height=5, font=myFont)
classify_text.grid(column=11, row=5)

export_text = tk.Label(window, width=20, height=5, font=myFont)
export_text.grid(column=6, row=5)

##---------
current_txt = tk.Label(window, text="Current Image: ", width=15, height=5, font=myFont)
current_txt.grid(column=10, row=1)

quality_lbl = tk.Label(window, text="Quality:", width=15, height=5, font=myFont)
quality_lbl.grid(column=10, row=5)

takepic_btn = tk.Button(window, text="Take Picture", width=11, height=2, font=myFont, command=clicked1)
takepic_btn.grid(column=1, row=1)

classify_btn = tk.Button(window, text="Classify Picture", width=13, height=2, font=myFont, command=clicked2)
classify_btn.grid(column=1, row=3)

export_btn = tk.Button(window, text="Export CSV", width=11, height=2, font=myFont, command=clicked3)
export_btn.grid(column=1, row=5)



# #black screen image import
# image1 = Image.open("blackscreen.jpeg")
# resizephoto = image1.resize((150, 150))
# photo = ImageTk.PhotoImage(resizephoto)
#
# label1 = tk.Label(window, image=photo)
# label1.image = photo
# # Position image
# # label1.place(x=320, y=100)
# label1.grid(column=10, row=2)
#
# #white screen image import
# image2 = Image.open("greyscreen.jpeg")
# resizephoto = image2.resize((200,20))
# photo2 = ImageTk.PhotoImage(resizephoto)
# label2 = tk.Label(window, image=photo2)
# label2.image = photo2
# label2.grid(column=11, row=5)



window.mainloop()





#instructions of what to do:
# -3 buttons:
# -1) take picture button 

# -2) classify picture (good/bad)
# -3) Export all the data in file 