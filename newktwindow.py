


"""
Name: Samuel Hellqvist
Date: 09-03-2022
Info:
<new file for the hotel
everything is given name like this:
self.whatthisis_what-type-of-tkinter-element-thtis-is
>
"""

#importing everythinig from tkinter 
from encodings import utf_8
from enum import auto
import tkinter as tk
from tkinter import *

#everything will be udner this main class
class Main():
    def __init__(self):

        #creating the root where everything will be placed
        self.root = tk.Tk()

        #defining the pic that will later be the background image
        self.pic = PhotoImage(file="SolHotell/pictures/finstrand.png")

        self.text = tk.StringVar()
        self.text.set("")

        #making sure that the tkinter window will be in fullscreen
        self.root.attributes("-fullscreen", True)

        #creating the background label that will make the background to the image
        self.bg_label = tk.Label(self.root, image=self.pic)
        self.bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        #creating the label with the headline
        self.header_label = tk.Label(self.root, text="☀" + "Sammys" + " "*3 + "solhotell" + "☀", fg="orange", font=("Broadway", 50), bg='medium blue')

        #creating the exit button, this button will have the command escape
        self.exit_button = tk.Button(self.root, text="exit", command=self.escape, fg="red", bg="white", width=10)

        #creating a button wich will show all the rooms
        self.room_button = tk.Button(self.root, text="UPPTÄCK VÅRA RUM", width=20, command=self.view, bg="orange", fg="white", font="Arial")

        #creating a button that will let the user check out
        self.checkout_button = tk.Button(self.root, text="CHECKA UT", width=20, command=self.checkout, bg="orange", fg="white", font="Arial")

        #creating the frame that will contain infromation about the room
        self.information_frame = tk.Frame(self.root, background="yellow")

        #creating the label that will show information about the deluxeroom
        self.roominformation_label = tk.Label(self.information_frame, textvariable=self.text, font=("Arial", 10))

        #creating a button that will be used to show information about the luxurious room
        self.deluxeroom_info_button = tk.Button(self.information_frame, text="Deluxerum", command=self.deluxe_info, padx=30, font=("Arial", 12))
        #this bit of code lets ut hide the button until we need it
        self.deluxeroom_info_button.pack_forget()

        self.economyroom_info_button = tk.Button(self.information_frame, text="Standardrum", command=self.standard_info, padx=30, font=("Arial", 12))
        self.economyroom_info_button.pack_forget()

        self.familyroom_info_button = tk.Button(self.information_frame, text="Familjerum", command=self.family_info, padx=30, font=("Arial", 12))
        self.familyroom_info_button.pack_forget()
        
        self.closeinfoframe_button = tk.Button(self.information_frame, text="x", command=self.closeinfoframe, fg=("red"), font=("Arial", 12))
        self.closeinfoframe_button.pack_forget()

        #packing all the tkinter elements and palcing them
        self.header_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.exit_button.place(relx=0.9, rely=0.9)
        self.room_button.place(relx=0.2, rely=0.5)
        self.checkout_button.place(relx=0.2, rely=0.6)

    #function that makes the program run
    def run(self):
        self.root.mainloop()

    #function that closes the tkinter window
    def escape(self):
        self.root.destroy()

    #funtion
    def view(self):
        self.information_frame.place(relx=0.4, rely=0.5)
        self.deluxeroom_info_button.grid(row=0, column=0)
        self.economyroom_info_button.grid(row=0, column=1)
        self.familyroom_info_button.grid(row=0, column=2)
        self.text.set("Klicka på någon av knapparna för att få information om det rummet")
        self.roominformation_label.grid(row=1, column=0, columnspan=4)
        self.closeinfoframe_button.grid(row=0, column=3)

    #function
    def checkout(self):
        pass

    def deluxe_info(self):
        f=open('SolHotell/deluxeroom.txt', encoding='utf-8')
        newtext= "\n" + f.read() + "\n"
        self.text.set(newtext)
    
    def standard_info(self):
        pass

    def family_info(self):
        pass

    def closeinfoframe(self):
        pass

app=Main()
app.run()