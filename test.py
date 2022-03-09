from email import header


"""
Name: Samuel Hellqvist
Date: 09-03-2022
Info:
<new file for the hotel
everything is given name like this:
self.whatthisis_what-type-of-tkinter-element-thtis-is
>
"""
import tkinter as tk
from tkinter import *
class Test():
    def __init__(self):

        self.root = tk.Tk()

        self.pic = PhotoImage(file="SolHotell/pictures/finstrand.png")

        self.text = tk.StringVar()
        self.text.set("")

        self.root.attributes("-fullscreen", True)

        self.bg_label = tk.Label(self.root, image=self.pic)
        self.bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        self.header_label = tk.Label(self.root, text="☀" + "Sammy's" + " "*3 + "solhotell" + "☀", fg="orange", font=("Broadway", 50), bg='medium blue')

        self.button = tk.Button(self.root, text="Click to change text below",command=self.changeText)

        self.exit_button = tk.Button(self.root, text="exit", command=self.escape, fg="red", bg="white", width=10)

        self.room_button = tk.Button(self.root, text="UPPTÄCK VÅRA RUM", width=20, command=self.view, bg="orange", fg="white", font="Arial")

        self.checkout_button = tk.Button(self.root, text="CHECKA OUT", width=20, command=self.checkout, bg="orange", fg="white", font="Arial")

        self.information_frame = tk.Frame(self.root, bg="green")

        self.deluxeroom_label = tk.Label(self.information_frame, textvariable=self.text)
        self.deluxeroom_label.pack()

        self.button.pack()
        self.header_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.exit_button.place(relx=0.9, rely=0.9)
        self.room_button.place(relx=0.2, rely=0.5)
        self.checkout_button.place(relx=0.2, rely=0.6)
        self.information_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.mainloop()

    def changeText(self):
        self.text.set("luxurious room")
        self.information_frame.place(relx=0.4, rely=0.3)  

    def escape(self):
        self.root.destroy()

    def view(self):
        pass

    def checkout(self):
        pass

app=Test()