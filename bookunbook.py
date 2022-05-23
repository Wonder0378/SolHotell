"""
Created by: Marcus Hedquist & Samuel Hellqvist
Date: 21-03-22

type = roomtype (Standard, Deluxe, Familyrum)
rooms = the amount of rooms in the "room"
beds = the amount of beds
wifi = 1/0 yes or no
bld = breakfast / lunch / dinner (0 nothing, 1 breakfast only, 2 breakfast & lunch, 3 everything)
fridge = 1/0 yes or no
roomid = room id
"""
import tkinter as tk
from tkinter import * 
from random import randint
from tkinter import messagebox as msgbox

class Room:
    
    """
    Class to create instances for every room at the hotel
    """
    def __init__(self, type, rooms, beds, wifi, bld, fridge, roomid):
        """
        Constructor to make the rooms
        @param type: The type of room, ranging from 1-3 (int)
        @param rooms: The amount of rooms in the "room" (int)
        @param beds: the amount of beds (int)
        @param wifi: true or false, but represented as 1 or 0 (int)
        @param bld: look at the explanation at the top of the script (int)
        @param fridge: true or false 0 / 1 (int)
        @param roomid: room Id(int)
        @return: void
        """
        # Colors
        self.carrot = "#ff8e00" #lightest orange
        self.orange = "#fd7702" #medium orange
        self.mandarin = "#ff5003" #darkest orange
        self.sky = "#5b84c4" #lightest blue
        self.blue = "#003f7d" #darkest blue
        self.white = "#ebebeb" #white/grey
        
        # Room information
        self.type = type
        self.rooms = rooms
        self.beds = beds
        self.wifi = wifi
        self.bld = bld
        self.fridge = fridge
        self.roomid = roomid

        # Room information as stringvalues
        self.str_t = "t{}".format(self.type)
        self.str_r = "r{}".format(self.rooms)
        self.str_b = "b{}".format(self.beds)
        self.str_w = "w{}".format(self.wifi)
        self.str_bld = "B{}".format(self.bld)
        self.str_f = "f{}".format(self.fridge)
        self.str_room = "R{}".format(self.roomid)

        # Complete string of room information
        self.string = self.str_t+self.str_r+self.str_b+self.str_w+self.str_bld+self.str_f+self.str_room

    def register(self):
        """
        Method to register the room to the savefile
        @return: void 
        """
        room_open = open('SolHotell/rooms.txt', 'a', encoding='utf-8')
        room_open.write("{}\n".format(self.string))
        room_open.close()

    def book(self, id, string):
        """
        Method to handle the booking of the room, which is initiated when
        the "boka" button is pressed. Method creates a separate window for
        the user to input his personal information aswell as the dates which
        he/she will stay at the hotel.
        @param id: the user id
        @param string: the string containing the information of the room, also exists
        as self.string. 
        @return: void
        """
        self.id = id
        class ClassMain:
            """
            Class to handle seperate booking window allowing the user
            to input booking data. 
            """
            def __init__(self, root, string, booktext):
                """
                Constructor to create the menu.
                @param root: the window to attach the new window onto
                @param string: the string containing the rooms information
                @param booktext: 
                @return: void
                """
                self.string = string
                self.booktext = booktext
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

                #entryboxes for inputting check-in day
                self.day_entry = Entry(topFrame)
                self.day_entry.grid(row=5, column=1, sticky= W)

                #Same as with checking in, but now for checking out
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
                """
                Method to save booking information to savefiles, removing room information from
                the file containing bookable rooms and inserting it together with user ID to file
                for booked rooms, aswell as inputting user to file containing users. 
                @return: void
                """
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

                    # Person details saved
                    toFile = open("SolHotell/people.txt", "a", encoding="utf-8")
                    toFile.write(self.name_entry.get() + "|" + self.email_entry.get() + "|" + self.adress_entry.get() + "|" + "incheckning: " + self.day_entry.get() + " " + self.month_var.get() + "|" + "utcheckning: " + self.day2_entry.get() + " " + self.month2_var.get() +  "|" + str(id) + "\n")
                    toFile.close()

                    # Removes the room from the list of avaiable rooms to book
                    with open("SolHotell/rooms.txt", "r") as f:
                        lines = f.readlines()
                    with open("SolHotell/rooms.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != self.string:
                                f.write(line)

                    # Adds room to list of currently booked
                    file_open = open('SolHotell/bookroom.txt', 'a')

                    self.str_id = "i{}".format(id)
                    self.string = self.string+self.str_id

                    file_open.write("{}\n".format(self.string))
                    file_open.close()

                    self.booktext.pack_forget()

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
        code = ClassMain(root, string, self.booktext)
        root.mainloop()

    def checkout(self, id):
        """
        Method to remove room from bookedrooms savefile and re-insert it into the save-
        file for bookable rooms. 
        @param id: user id
        @return: void
        """
        print(id)

        # Removing room from booked savefile
        with open("SolHotell/bookroom.txt", "r") as f:
            lines = f.readlines()
        with open("SolHotell/bookroom.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "{}i{}".format(self.string, id):
                    f.write(line)
        # Re-registering room to bookable savefile
        self.register()

        self.booktext.pack_forget()

    def appear(self, frame, order, type):
        """
        Method to make the room visible on the page where the user
        can book the rooms.
        @param frame: the frame which the room will be put on
        @param order: the order in which the rooms will be showcased (may or may not be included in final draft)
        @param type: roomtype as a string (only used to type out roomtype)
        @return: void
        """
        self.booktext = tk.Frame(frame)
        self.booktext.pack(pady=5)

        # Converting the room information into actually readable text
        if self.wifi == 1:
            iswifi = "Free Wifi"
        else:
            iswifi = "No Wifi"

        if self.fridge == 1:
            isfridge = "Fridge"
        else:
            isfridge = "No Fridge"

        if self.bld == 0:
            bld = "No breakfast"
        elif self.bld == 1:
            bld = "Breakfast"
        elif self.bld == 2:
            bld = "Breakfast and lunch"
        else:
            bld = "Breakfast, lunch and dinner"

        # Creating the visual framework where the information is showcased
        self.front = tk.Label(self.booktext, text=type.upper()+"room".upper(), bg=self.white, font="Arial, 11")
        self.moreinfo = tk.Label(self.booktext,bg=self.white, text="Rooms: {} | Beds: {} | {} | {} | {}".format(self.rooms, self.beds, iswifi, isfridge, bld))

        self.bookbtn = tk.Button(self.booktext, text="BOKA", command=lambda : self.book(randint(1, 1000), self.string), bg=self.carrot, fg=self.white, font="Arial, 10", padx=20)
        self.bookbtn.grid(column=5, row=1,)

        self.front.grid(column=0, row=0)
        self.moreinfo.grid(column=0, row=1)

    def unbookappear(self, frame, type, fromtime, totime, id):
        """
        Similair to the appear method, the method makes the room visible
        on the page where the user can choose to unbook a room. 
        @param frame: the frame on which the room will be put
        @param type: the type of room to unbook
        @param fromtime: date of check-in
        @param totime: date of checkout
        @param id: user id
        @return: void
        """

        self.booktext = tk.Frame(frame)
        self.booktext.pack(pady=5)
        self.id = id

        # Converts roomvalues to actually readable text
        if int(type) == 1:
            type = "Standard"
        elif int(type) == 2:
            type = "Deluxe"
        else:
            type = "Family"

        if self.wifi == 1:
            iswifi = "Free Wifi"
        else:
            iswifi = "No Wifi"

        if self.fridge == 1:
            isfridge = "Fridge"
        else:
            isfridge = "No Fridge"

        if self.bld == 0:
            bld = "No breakfast"
        elif self.bld == 1:
            bld = "Breakfast"
        elif self.bld == 2:
            bld = "Breakfast and lunch"
        else:
            bld = "Breakfast, lunch and dinner"

        # Setting up visual framework to showcase information
        self.front = tk.Label(self.booktext, text=type.upper()+"room".upper(), bg=self.white, font="Arial, 11")
        self.moreinfo = tk.Label(self.booktext,bg=self.white, text="Rooms: {} | Beds: {} | {} | {} | {}".format(self.rooms, self.beds, iswifi, isfridge, bld))
        self.evenmoreinfo = tk.Label(self.booktext, text=fromtime + " - " + totime)
        self.unbook = tk.Button(self.booktext, text="Avboka", command=lambda : self.checkout(self.id))
        self.unbook.pack_forget()

        self.front.grid(column=0, row=0)
        self.moreinfo.grid(column=0, row=1)
        self.evenmoreinfo.grid(column=0, row=2)
        self.unbook.grid(column=5, row=1)