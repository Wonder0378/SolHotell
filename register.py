from tkinter import *
import tkinter.messagebox as msgbox

class Main:
    def __init__(self, root):
        root.wm_title("Användarinormation")

        topFrame = Frame(root)
        topFrame.pack()

        bottomFrame = Frame(root)
        bottomFrame.pack()
        
        #bygger topframen

        lblName = Label(topFrame, text="Förnamn: ")
        lblName.grid(row = 0, column= 0, sticky = W)

        lblPersonnummer = Label(topFrame, text="Efternamn: ")
        lblPersonnummer.grid(row = 1, column = 0, sticky = W)

        lblAdress = Label(topFrame, text="Adress: ")
        lblAdress.grid(row = 2, column = 0, sticky = W)

        self.entName = Entry(topFrame)
        self.entName.grid(row = 0, column = 1)

        self.entNummer = Entry(topFrame)
        self.entNummer.grid(row = 1, column = 1)

        self.entAdress = Entry(topFrame)
        self.entAdress.grid(row = 2, column = 1)

        Alabel = Label(topFrame, text="Inchecking: ")
        Alabel.grid(row = 3, column = 0, sticky = W)

        self.variable = StringVar(topFrame)
        self.variable.set("Månad")
        self.dropit = OptionMenu(topFrame, self.variable, "Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec")
        self.dropit.grid(row=4, column=0)

        #bygger bottomframe

        btnSave = Button(bottomFrame, text = "Boka", width = 10, command=self.saveToFile)
        btnSave.pack(pady=2)

    def saveToFile(self):
        if self.entName.get()==(""):
            msgbox.showinfo("Error", "Inget namn angett")
            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

        elif self.entNummer.get()==(""):
            msgbox.showinfo("Error", "Inget personummer angett")
            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

        elif self.entAdress.get()==(""):
            msgbox.showinfo("Error", "Ingen adress anged")
            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

        else: 
            toFile = open("phonobook.txt", "a")
            toFile.write(self.entName.get() + " " + self.entNummer.get() + " " + self.entAdress.get() + self.variable.get() + "\n")
            toFile.close()

            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

            msgbox.showinfo("Succes", "Personen är sparad till filen")

root = Tk()
Main(root)
root.mainloop()