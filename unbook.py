from tkinter import *
import tkinter.messagebox as msgbox

class Main:
    def __init__(self, root):
        root.wm_title("Avbryta bokning")

        #Set the geometry of frame
        root.geometry("200x150")

        #Set the resizable property False
        root.resizable(False, False)

        #building two frames that the window will have
        topFrame = Frame(root)
        topFrame.pack()
        
        #creating labels and entrys for the user information
        name_lable = Label(topFrame, text="Namn: ")
        name_lable.grid(row = 0, column= 0, sticky = W)

        email_lable = Label(topFrame, text="E-mail: ")
        email_lable.grid(row = 1, column = 0, sticky = W)

        unbook_btn = Button(topFrame, text="Gå vidare", command=self.unbook)
        unbook_btn.grid(row=2, column=1, sticky = W, pady="10")

        self.name_entry = Entry(topFrame)
        self.name_entry.grid(row = 0, column = 1)

        self.email_entry = Entry(topFrame)
        self.email_entry.grid(row = 1, column = 1)

    def unbook(self):
        print(self.name_entry.get())
        print(self.email_entry.get())
        #msgbox.showinfo("Klart!", "Din bokning är nu avbruten!")
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        root.destroy()

root = Tk()
Main(root)
root.mainloop()