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
        window.geometry("720x720")

        #color of window
        window['background'] = "#3686c7"

        #----------------------Button layout------------------------------
        for i in range(15):
            window.grid_columnconfigure(i, weight=1)
            window.grid_rowconfigure(i, weight=1)

        takePictureBtn = tk.Button(window, text="Take Picture", width=20, height=2, font=myFont, command=self.takePicture)
        takePictureBtn.grid(column=0, row=10, sticky="nsew")

        classifyPictureBtn = tk.Button(window, text="Classify Picture", width=20, height=2, font=myFont,command=self.categorize)
        classifyPictureBtn.grid(column=1, row=10, sticky="nsew")

        exportCsvBtn = tk.Button(window, text="Export CSV", width=20, height=2, font=myFont, command=self.export)
        exportCsvBtn.grid(column=2, row=10, sticky="nsew")

        #-----quality text------
        self.quality_text = Label(window, bg = '#f9efd2', fg = 'black', text="Quality:") #return quality:bad/good
        self.quality_text.grid(column=2, row=5, sticky="nsew")

        self.quality_box = tk.StringVar()  # integer
        self.quality_box.set("")
        self.quality_entry = tk.Entry(window, textvariable=self.quality_text, font=('calibre', 10, 'normal'), highlightbackground = "black")
        self.quality_entry.grid(column=2, row=6, sticky="nsew")

        self.currentImage_text = Label(window, text="Current Image:(_/_)") #add image number
        self.currentImage_text.grid(column=2, row=3, sticky="nsew")
        self.currentImage_box = tk.IntVar()  # integer
        self.currentImage_box.set("")
        self.currentImage_entry = tk.Entry(window, textvariable=self.currentImage_text, font=('calibre', 10, 'normal'), highlightbackground = "black")
        self.currentImage_entry.grid(column=3, row=3, sticky="nsew")
        # ----------------------Grey screen------------------------------

        # grey screen image import
        greyimage = Image.open("greyscreen.jpeg")
        resizephoto1 = greyimage.resize((200, 200))
        photo1 = ImageTk.PhotoImage(resizephoto1)

        #image display
        self.canvas = Canvas(window, width = 200, height = 200)
        self.canvas.grid(column=2, row=4, sticky="nesw")
        self.canvas.create_image(100,100,image=photo1)

        #------------------------black screen-------------------
        self.SegmentationLbl = tk.Label(window, text="Segmentation fault: ", width=20, height=2, font=myFont)
        self.SegmentationLbl.grid(column=0, row=3, sticky="esw")

        blackimage = Image.open("blackscreen.jpeg")
        resizephoto = blackimage.resize((200, 200))
        photo = ImageTk.PhotoImage(resizephoto)

        # image display
        self.canvas = Canvas(window, width=150, height=200)
        self.canvas.grid(column=0, row=4,sticky="nsew")
        self.canvas.create_image(100, 100, image=photo)


        #---------------------PartID----------------------------
        #partID text
        self.partID_text = Label(window, text="PartID: ")
        self.partID_text.grid(column=0, row=1, sticky="nsew")

        #labeled partid input box
        self.partID_box = tk.StringVar() #String
        self.partID_box.set("")
        self.partID_entry = tk.Entry(window, textvariable=self.partID_text, font=('calibre', 10, 'normal'), highlightbackground = "black")
        self.partID_entry.grid(column=1, row=1, sticky="nsew")

        # ---------------------Orientation ----------------------------
        # orientation text
        self.orientation_text = Label(window, text="Orientation: ")
        self.orientation_text.grid(column=0, row=2, sticky="nsew")
        # labeled orientation
        self.orientation_box = tk.IntVar() #integer
        self.orientation_box.set("")
        self.orientation_entry = tk.Entry(window, textvariable=self.orientation_text, font=('calibre', 10, 'normal'), highlightbackground = "black")
        self.orientation_entry.grid(column=1, row=2, sticky="nsew")

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

    def getPartInfo(self):
        return [self.partID_entry.get(), self.orientation_entry.get()]
    
Display()