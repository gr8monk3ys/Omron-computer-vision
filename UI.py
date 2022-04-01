import tkinter as tk
import tkinter.font as font
from tkinter import *
from PIL import Image, ImageTk
from apiTest import Interface

class Display:
    def __init__(self):
        self.api = Interface()
        window = tk.Tk()
        window.title("Omron UI")

        myFont = font.Font(family='Helvetica')

        window.geometry("512x512")

        for i in range(13):
            window.grid_columnconfigure(i, weight=2)
            window.grid_rowconfigure(i, weight=1)

        self.new_text = tk.Label(window, width=15, height=5, font=myFont)
        self.new_text.grid(column=6, row=1)

        self.new_text2 = tk.Label(window, width=15, height=5, font=myFont)
        self.new_text2.grid(column=6, row=5)

        self.new_text3 = tk.Label(window, width=15, height=5, font=myFont)
        self.new_text3.grid(column=6, row=6)

        lbl = tk.Label(window, text="Current Image: ", width=15, height=5, font=myFont)
        lbl.grid(column=4, row=1)

        btn1 = tk.Button(window, text="Take Picture", width=11, height=2, font=myFont, command=self.picture_taken)
        btn1.grid(column=1, row=1)

        btn2 = tk.Button(window, text="Classify Picture", width=13, height=2, font=myFont, command=self.categorize)
        btn2.grid(column=1, row=3)

        btn3 = tk.Button(window, text="Export CSV", width=11, height=2, font=myFont, command=self.export)
        btn3.grid(column=1, row=5)

        self.quality_lbl = tk.Label(window, text="Quality:", width=15, height=5, font=myFont)
        self.quality_lbl.grid(column=4, row=5)

        # black screen image import
        image = Image.open("golden_frieza.jpg")
        resizephoto = image.resize((150, 150))
        photo = ImageTk.PhotoImage(resizephoto)

        self.label1 = tk.Label(window, image=photo)
        self.label1.image = photo
        # Position image
        # label1.place(x=320, y=100)
        self.label1.grid(column=10, row=2)

        window.mainloop()

    def picture_taken(self):
        self.label1.image = self.api.load_pic()
        #self.new_text.configure(text="Picture taken")

    def categorize(self):
        self.quality_lbl = self.api.classify_pic()
        #self.new_text2.configure(text="good/bad")

    def export(self):
        self.api.get_data()
        #self.new_text3.configure(text="exporting")


a = Display()


