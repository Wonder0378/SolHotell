"""
Created by: Samuel Hellqvist and Marcus Hedquist
Date: 09-03-2022
Info:

new file for the hotel
everything is given name like this:

self.what-this-is_what-type-of-tkinter-element-thtis-is

"""

#importing everythinig from tkinter 
import tkinter as tk
from tkinter import *

#everything will be udner this main class
class Main():
    def __init__(self):

        self.title = "Solhotellet, Marcus och Samuel"

        #creating the root where everything will be placed
        self.root = tk.Tk()

        #defining the pic that will later be the background image
        self.pic = PhotoImage(file="SolHotell/pictures/finstrand.png")

        self.carrot = "#ff8e00" #lightest orange
        self.orange = "#fd7702" #medium orange
        self.mandarin = "#ff5003" #darkest orange

        self.sky = "#5b84c4" #lightest blue
        self.blue = "#003f7d" #darkest blue

        self.white = "#ebebeb" #white/grey

        self.secondarybtn = "green"
        self.red = "red"
        #text variable
        self.text = tk.StringVar()
        self.text.set("")

        #making sure that the tkinter window will be in fullscreen
        self.root.attributes("-fullscreen", True)

        #creating the background label that will make the background to the image
        self.bg_label = tk.Label(self.root, image=self.pic)
        self.bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        #creating the label with the headline
        self.header_label = tk.Label(self.root, text="☀" + "SAMMYS" + " "*3 + "SOLHOTELL" + "☀", bg=self.blue, fg=self.carrot, font=("Broadway", 50))

        #creating the exit button, this button will have the command escape
        self.exit_button = tk.Button(self.root, text="EXIT", command=self.escape, width=10, bg=self.carrot, fg="black")

        #creating a button wich will show all the rooms
        self.roominfo_button = tk.Button(self.root, text="CHECKA IN", width=20, command=self.view, bg=self.carrot, fg=self.white, font="Arial")

        #creating a button that will let the user check out
        self.checkout_button = tk.Button(self.root, text="CHECKA UT", width=20, command=self.checkout, bg=self.carrot, fg=self.white, font="Arial")

        #packing all the tkinter elements and palcing them
        self.header_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.exit_button.place(relx=0.9, rely=0.9)
        self.roominfo_button.place(relx=0.2, rely=0.5)
        self.checkout_button.place(relx=0.2, rely=0.6)

    #function that makes the program run
    def run(self):
        self.root.mainloop()

    #function that closes the tkinter window
    def escape(self):
        self.root.destroy()

    #funtion to view all different rooms
    def view(self):
        #creating the frame that will contain infromation about the room
        self.information_frame = tk.Frame(self.root, background=self.white)

        #creating the label that will show information about the deluxeroom
        self.roominformation_frame = tk.Frame(self.information_frame, background="#E7E0DB")

        #creating a button that will display informatoin about the standard room
        self.economyroom_info_button = tk.Button(self.information_frame, text="Standardrum", command=self.standard_info, padx=30, font=("Arial", 12), bg=self.sky, fg=self.white)
        self.economyroom_info_button.pack_forget()

        #creating a button that will be used to show information about the luxurious room
        self.deluxeroom_info_button = tk.Button(self.information_frame, text="Deluxerum", command=self.deluxe_info, padx=30, font=("Arial", 12), bg=self.sky, fg=self.white)
        #this bit of code lets ut hide the button until we need it
        self.deluxeroom_info_button.pack_forget()
        
        #creating a button that will display information about the family room
        self.familyroom_info_button = tk.Button(self.information_frame, text="Familjerum", command=self.family_info, padx=30, font=("Arial", 12), bg=self.sky, fg=self.white)
        self.familyroom_info_button.pack_forget()

        #creating a button that will be closing the information frame
        self.closeinfoframe_button = tk.Button(self.information_frame, text="x", command=self.closeinfoframe, fg="red", font=("Arial", 12))
        self.closeinfoframe_button.pack_forget()

        #creating the information frame and packing everythin
        self.information_frame.place(relx=0.4, rely=0.5)
        self.economyroom_info_button.grid(row=0, column=0)
        self.deluxeroom_info_button.grid(row=0, column=1)
        self.familyroom_info_button.grid(row=0, column=2)
        self.text.set( "\n Klicka på någon av knapparna för att få information om det rummet \n")
        self.roominformation_frame.grid(row=1, column=0, columnspan=4)
        self.closeinfoframe_button.grid(row=0, column=3)

    #function for checkout
    def checkout(self):
        pass
    
    #function for viewing information about the standard room
    def standard_info(self):
        #opening the file that will contain the information we want to show
        f=open('SolHotell/z_standardroom.txt', encoding='utf-8')
        newtext = "\n" + f.read() + "\n"
        self.text.set(newtext)
        #creating and adding a button that will be used for booking a room
        self.book_button = tk.Button(self.information_frame, text="Boka", command=self.bookroom, font=("Arial"), bg=self.carrot, fg=self.white)
        self.book_button.grid(row=3, column=1)

    #function for viewing information about the family room
    def family_info(self):
        #creating and adding a button that will be used for booking a room
        f=open('SolHotell/z_familyroom.txt', encoding='utf-8')
        newtext = "\n" + f.read() + "\n"
        self.text.set(newtext)
        #creating and adding a button that will be used for booking a room
        self.book_button = tk.Button(self.information_frame, text="Boka", command=self.bookroom, font=("Arial"), bg=self.carrot, fg=self.white)
        self.book_button.grid(row=3, column=1)

    #function for viewing information about the deluxe room
    def deluxe_info(self):
        #opening the file that will contain the information we want to show
        f=open('SolHotell/z_deluxeroom.txt', encoding='utf-8')
        newtext = "\n" + f.read() + "\n"
        self.text.set(newtext)
        #creating and adding a button that will be used for booking a room
        self.book_button = tk.Button(self.information_frame, text="Boka", command=self.bookroom, font=("Arial"), bg=self.carrot, fg=self.white)
        self.book_button.grid(row=3, column=1)

    #funtion that will close the information frame
    def closeinfoframe(self):
        #the information frame will be destroyed, it will be created again when the show information button will be clicked
        self.information_frame.destroy()

    #function that books the room
    def bookroom(self):
        pass

#setting 'app' to equal main
app=Main()
#using the run funciton on app
app.run()