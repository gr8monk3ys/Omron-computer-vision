import tkinter as tk
import tkinter.font as font
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image
from PIL import ImageTk
from API import Interface
import cv2 as cv

class Display:
    # -------------------window---------------------------------
    def __init__(self):
        self.api = Interface()
        window = tk.Tk()
        window.title("Omron UI")
        myFont = font.Font(family='Helvetica')
        window.geometry("512x512") #size of window

        #----------------------Button layout------------------------------
        for i in range(13):
            window.grid_columnconfigure(i, weight=1) #2 ?
            window.grid_rowconfigure(i, weight=1)

        self.currentImageLbl = tk.Label(window, width=15, height=5, font=myFont)
        self.currentImageLbl.grid(column=6, row=1)
        #
        # self.takePictureLbl = tk.Label(window, width=15, height=5, font=myFont)
        # self.takePictureLbl.grid(column=6, row=5)
        #
        self.classifyPictureLbl = tk.Label(window, width=15, height=5, font=myFont)
        self.classifyPictureLbl.grid(column=6, row=6)

        takePictureBtn = tk.Button(window, text="Take Picture", width=11, height=2, font=myFont, command=self.takePicture)
        takePictureBtn.grid(column=0, row=3)

        classifyPictureBtn = tk.Button(window, text="Classify Picture", width=13, height=2, font=myFont,command=self.categorize)
        classifyPictureBtn.grid(column=0, row=4)

        exportCsvBtn = tk.Button(window, text="Export CSV", width=11, height=2, font=myFont, command=self.export)
        exportCsvBtn.grid(column=0, row=5)

        self.quality_lbl = tk.Label(window, text="Quality:", width=15, height=5, font=myFont)
        self.quality_lbl.grid(column=0, row=6)

        # ----------------------Black screen------------------------------
        #current image text shoudl be next to black screen
        self.currentImageLbl = tk.Label(window, text="Current Image: ", width=16, height=5, font=myFont)
        self.currentImageLbl.grid(column=3, row=2)

        # black screen image import
        image = Image.open("greyscreen.jpeg")
        resizephoto = image.resize((200, 200))
        photo = ImageTk.PhotoImage(resizephoto)

        #image display
        self.canvas = Canvas(window, width = 200, height = 200)   
        self.canvas.grid(row=3,column=3)
        self.canvas.create_image(100,100,image=photo)
        #---------------------PartID----------------------------
        #partID text
        self.partID_text = Label(window, text="PartID: ")
        self.partID_text.grid(column=0, row=1)

        #labeled partid input box
        self.partID_box = tk.StringVar() #String
        # name = name_var.get()
        self.partID_box.set("")
        self.partID_entry = tk.Entry(window, textvariable=self.partID_text, font=('calibre', 10, 'normal'))
        self.partID_entry.grid(column=1, row=1)

        # ---------------------Orientation ----------------------------
        # orientation text
        self.orientation_text = Label(window, text="Orientation: ")
        self.orientation_text.grid(column=0, row=2)
        # labeled orientation
        self.orientation_box = tk.IntVar() #integer
        # name = name_var.get()
        self.orientation_box.set("")
        self.orientation_entry = tk.Entry(window, textvariable=self.orientation_text, font=('calibre', 10, 'normal'))
        self.orientation_entry.grid(column=1, row=2)

        window.mainloop()

    def takePicture(self):
        [partid,ori] = self.getPartInfo()
        im = self.api.takePicture(partid,ori)
        im = cv.resize(im,(200,200))
        photo = ImageTk.PhotoImage(Image.fromarray(im))
        self.canvas.create_image(100,100,image=photo)   
        self.canvas.itemconfigure(self.canvas, image=photo)
        self.classifyPictureLbl.configure(text="")
        
    def categorize(self):
        [partid,ori] = self.getPartInfo()
        res = self.api.classify_img(partid,ori)
        mp = ['bad', 'good']
        self.classifyPictureLbl.configure(text=mp[res])

    def export(self):
        self.api.saveCSV()
        #self.new_text3.configure(text="exported")

    def getPartInfo(self):
        return [self.partID_entry.get(), self.orientation_entry.get()]
    
Display()