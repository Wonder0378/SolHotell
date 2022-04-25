from tkinter import *
import tkinter.messagebox as msgbox

class Main:
    def __init__(self, root):
        root.wm_title("Bokning")

        #Set the geometry of frame
        root.geometry("250x250")

        #Set the resizable property False
        root.resizable(False, False)

        #building two frames that the window will have
        topFrame = Frame(root)
        topFrame.pack()

        bottomFrame = Frame(root)
        bottomFrame.pack()
        
        #creating labels and entrys for the user information
        name_lable = Label(topFrame, text="Namn: ")
        name_lable.grid(row = 0, column= 0, sticky = W)

        email_lable = Label(topFrame, text="E-mail: ")
        email_lable.grid(row = 1, column = 0, sticky = W)

        adress_lable = Label(topFrame, text="Adress: ")
        adress_lable.grid(row = 2, column = 0, sticky = W)

        #placing the names and entrys
        self.name_entry = Entry(topFrame)
        self.name_entry.grid(row = 0, column = 1)

        self.email_entry = Entry(topFrame)
        self.email_entry.grid(row = 1, column = 1)

        self.adress_entry = Entry(topFrame)
        self.adress_entry.grid(row = 2, column = 1)

        #creating labels for checking and placing them
        checkin_label = Label(topFrame, text="Inchecking: ")
        checkin_label.grid(row = 3, column = 0, sticky = W)
        month_label = Label(topFrame, text="Månad: ")
        month_label.grid(row=4, column=0, sticky= W)
        day_label = Label(topFrame, text="Dag: ")
        day_label.grid(row=4, column=1)

        #a dropdown menue is used for choosing months
        self.month_var = StringVar(topFrame)
        self.month_var.set("Månad")
        #here every month of the year is available as an option
        self.month_optionsmenu = OptionMenu(topFrame, self.month_var, "Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec")
        self.month_optionsmenu.grid(row=5, column=0)
        
        self.day_entry = Entry(topFrame)
        self.day_entry.grid(row=5, column=1, sticky= W)

        checkout_label = Label(topFrame, text="Utchecking: ")
        checkout_label.grid(row = 6, column = 0, sticky = W)
        month2_label = Label(topFrame, text="Månad: ")
        month2_label.grid(row=7, column=0, sticky= W)
        day2_label = Label(topFrame, text="Dag: ")
        day2_label.grid(row=7, column=1)

        self.month2_var = StringVar(topFrame)
        self.month2_var.set("Månad")
        self.month2_optionsmenu = OptionMenu(topFrame, self.month2_var, "Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec")
        self.month2_optionsmenu.grid(row=9, column=0)
        
        self.day2_entry = Entry(topFrame)
        self.day2_entry.grid(row=9, column=1, sticky= W)

        #this button is used to save the booking
        save_btn = Button(bottomFrame, text = "Boka", width = 10, command=self.saveToFile)
        save_btn.pack(pady=2)

    #saving the booking to a file
    def saveToFile(self):
        #if a name has not been added, you cant book
        if self.name_entry.get()==(""):
            msgbox.showinfo("Error", "Inget namn angett")
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.adress_entry.delete(0, END)
            self.day_entry.delete(0, END)
            self.name_entry.focus_set()

        #if an emial-adress has not been added, you cant book
        elif self.email_entry.get()==(""):
            msgbox.showinfo("Error", "Inget e-mail adress angett")
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.adress_entry.delete(0, END)
            self.day_entry.delete(0, END)
            self.name_entry.focus_set()

        #if an adress has not been added, you cant book
        elif self.adress_entry.get()==(""):
            msgbox.showinfo("Error", "Ingen adress anged")
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.adress_entry.delete(0, END)
            self.day_entry.delete(0, END)
            self.name_entry.focus_set()

        #if everything is added properly, the booking is saved to a file
        else: 
            toFile = open("SolHotell/bookings.txt", "a", encoding="utf-8")
            toFile.write(self.name_entry.get() + "|" + self.email_entry.get() + "|" + self.adress_entry.get() + "|" + "incheckning: " + self.day_entry.get() + " " + self.month_var.get() + "|" + "utcheckning: " + self.day2_entry.get() + " " + self.month2_var.get() +  "|" + "Id: " + "\n")
            toFile.close()

            #all the entrys are emptied so that they are ready for the next user
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.adress_entry.delete(0, END)
            self.day_entry.delete(0, END)
            self.day2_entry.delete(0, END)
            self.month_var.set("Månad")
            self.month2_var.set("Månad")
            self.name_entry.focus_set()
            
            #the user recieves a massage that declare the succesfull booking of a rooom
            msgbox.showinfo("Succes", "Du har nu bokat ett rum!")
            #the window is getting shutted down
            root.destroy()

root = Tk()
Main(root)
root.mainloop()