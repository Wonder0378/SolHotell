"""
Name: Samuel Hellqvist
Date: 18-02-2022
Info:
<Insert information about file>
"""
from tkinter import *
import tkinter.messagebox as msgbox
root=Tk()
from turtle import *
class Main:
    #pic = PhotoImage(file="pictures/mallorca.png")
    def check():
        msgbox.showinfo("Empty", "Rummet bokat!")
    root.geometry("850x500")
    my_label=Label(root, bg="blue")
    my_label.place(x=0, y=0, relheight=1, relwidth=1)

    my_headline = Label(root, text="Sammy's solhotell",fg="orange", font=("Helvetica", 40))
    my_headline.place(relx=0.5, rely=.3, anchor=CENTER)
    
    my_button = Button(root, text="upptäck våra rum", command=check)
    my_button.place(relx=.5, rely=.7, anchor= CENTER)

root.mainloop()