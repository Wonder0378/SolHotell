


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
        self.text.set(" ")

        #making sure that the tkinter window will be in fullscreen
        self.root.attributes("-fullscreen", True)

        #creating the background label that will make the background to the image
        self.bg_label = tk.Label(self.root, image=self.pic)
        self.bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        #creating the label with the headline
        self.header_label = tk.Label(self.root, text="☀" + "Sammys" + " "*3 + "solhotell" + "☀", fg="orange", font=("Broadway", 50), bg='medium blue')

        self.button = tk.Button(self.root, text="Click to change text below",command=self.changeText)

        #creating the exit button, this button will have the command escape
        self.exit_button = tk.Button(self.root, text="exit", command=self.escape, fg="red", bg="white", width=10)

        #creating a button wich will show all the rooms
        self.room_button = tk.Button(self.root, text="UPPTÄCK VÅRA RUM", width=20, command=self.view, bg="orange", fg="white", font="Arial")

        #creating a button that will let the user check out
        self.checkout_button = tk.Button(self.root, text="CHECKA OUT", width=20, command=self.checkout, bg="orange", fg="white", font="Arial")

        #creating the frame that will contain infromation about the room
        self.information_frame = tk.Frame(self.root, bg="green")

        #creating the label that will show information about the deluxeroom
        self.deluxeroom_label = tk.Label(self.information_frame, textvariable=self.text)
        self.deluxeroom_label.pack()

        #packing all the tkinter elements and palcing them
        self.button.pack()
        self.header_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.exit_button.place(relx=0.9, rely=0.9)
        self.room_button.place(relx=0.2, rely=0.5)
        self.checkout_button.place(relx=0.2, rely=0.6)
        self.information_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    #function that makes the program run
    def run(self):
        self.root.mainloop()

    #function
    def changeText(self):
        self.text.set("luxurious room")
        self.information_frame.place(relx=0.4, rely=0.3)  

    #function that closes the tkinter window
    def escape(self):
        self.root.destroy()

    #funtion
    def view(self):
        pass

    #function
    def checkout(self):
        pass


app=Main()
app.run()