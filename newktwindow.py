"""
Created by: Samuel Hellqvist and Marcus Hedquist
Date: 09-03-2022
Info:
new file for the hotel
everything is given name like this:
self.what-this-is_what-type-of-tkinter-element-thtis-is
"""

#imports what the program needs
import tkinter as tk
from tkinter import *
from bookunbook import Room
from random import randint
import turtle
from turtle import *

#trying to import the water-app 
#if the user does not have pip the weather app will not work
#this little piece code prevents the program from crashing if pip is not avilible
try:
    from getweather import GetWeather
except: 
    pass

#everything will be under this main class
class Main():
    """
    Class to create tkinter window
    """
    def __init__(self):
        """
        Method for placing tkinter elements
        """
        self.__roomids = [] #creating a list for the room id:s
        self.getrooms() #calling a method that fetches information about the rooms

        self.title = "Solhotellet, Marcus och Samuel"

        #creating the root where everything will be placed
        self.root = tk.Tk()

        #defining the pic that will later be the background image
        self.pic = PhotoImage(file="SolHotell/pictures/finstrand.png")

        #setting color variebles that will be used later
        
        self.carrot = "#ff8e00" #lightest orange
        self.orange = "#fd7702" #medium orange
        self.mandarin = "#ff5003" #darkest orange

        self.sky = "#5b84c4" #lightest blue
        self.blue = "#003f7d" #darkest blue

        self.white = "#ebebeb" #white/grey

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

        try: 
            #creates a widget where the current weather at the hotel is shown
            weather = GetWeather()
            self.weather_label = tk.Label(self.root, text="Vädret på hotellet just nu: \n" + weather.tempText + "°C" + "\n" + weather.weather, bg=self.sky, fg=self.white, font=("Arial, 11"))
        except:
            pass
        
        #creating the exit button, this button will have the command escape
        self.exit_button = tk.Button(self.root, text="EXIT", command=self.escape, width=10, bg=self.carrot, fg="black")

        #creating a button wich will show all the rooms
        self.roominfo_button = tk.Button(self.root, text="CHECKA IN", width=20, command=self.view, bg=self.carrot, fg=self.white, font="Arial")

        #creating a button that will let the user check out
        self.checkout_button = tk.Button(self.root, text="CHECKA UT", width=20, command=self.getcheckoutinfo, bg=self.carrot, fg=self.white, font="Arial")

        #placing the header
        self.header_label.place(relx=0.5, rely=0.17, anchor=CENTER)

        #this is done to not get an error if pip is not present
        #the programm tries to show the weather label
        #and if it can't be shownthe program simply skips it
        try: 
            self.weather_label.place(relx=0.145, rely=0.3)
        except:
            pass

        self.exit_button.place(relx=0.9, rely=0.9)
        self.roominfo_button.place(relx=0.2, rely=0.5)
        self.checkout_button.place(relx=0.2, rely=0.6)


    def roomid(self):
        """
        This function will crate a id for every room
        @return: void
        """
        while True:
            id = randint(1000, 9999)

            if id in self.__roomids:
                pass
            else:
                break

        return id


    def getrooms(self):
        """
        This function will create all the rooms for the program
        @return: void
        """

        #Inserting rooms
        self.standardrooms = []
        self.deluxerooms = []
        self.familyrooms = []
        self.bookedrooms = []

        #try: # Checks if there are any already registered rooms in the hotel
        try:
            with open("SolHotell/rooms.txt", "r", encoding="utf-8") as text:
                for i, line in enumerate(text.readlines()):
                    if line.endswith("\n"):
                        line = line.replace("\n", "")

                    type = int(line[1:2])
                    rooms = int(line[3:4])
                    beds = int(line[5:6])
                    wifi = int(line[7:8])
                    bld = int(line[9:10])
                    fridge = int(line[11:12])
                    roomid = int(line[13:17])

                    #Checks wich type of room it is and displaying correct information
                    if type == 1:
                        self.standardrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))
                    elif type == 2:
                        self.deluxerooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))
                    elif type == 3:
                        self.familyrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))

        except: # If file hasn't been created, or is empty, an exception will be made
            for i in range(1, 5): # And 4 rooms of every kind will be created
                self.standardrooms.append(Room(1, randint(1, 4), randint(2, 4), randint(0, 1), 1, randint(0, 1), self.roomid()))
                self.deluxerooms.append(Room(2, randint(4, 6), randint(2, 4), 1, randint(2, 4), 1, self.roomid()))
                self.familyrooms.append(Room(3, randint(3, 5), randint(3, 4), 1, randint(1, 4), randint(0, 1), self.roomid()))

            for i in self.standardrooms:
                i.register()
            for i in self.deluxerooms:
                i.register()
            for i in self.familyrooms:
                i.register()
        

    def run(self):
        """
        This method will make the program run using mainloop
        @return: void
        """
        self.root.mainloop()

    def escape(self):
        """
        This method will close the tkinter window
        @return: void
        """
        self.root.destroy()
        from theturtle import Turtle
        Turtle.run()

    def view(self):
        """
        This is a method used to veiw all the rooms
        They will be placed on the window
        @return: void
        """
        try:
            self.closeinfoframe()
            self.closecheckoutframe()
            """
            the information frame and checkout frame will be closed using these functions
            this is used to prevent the errors that will accure if 2 frames is open at once
            """
        except:
            pass
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
        self.roominformation_frame.grid(row=1, column=0, columnspan=5, sticky="w")
        self.closeinfoframe_button.grid(row=0, column=3)

    #function for checkout
    def getcheckoutinfo(self):
        """
        This method will create a frame that will be used to checkout
        @retun: void
        """
        try:
            self.closeinfoframe()
            self.closecheckoutframe()
            """
            the information frame and checkout frame will be closed using these functions
            this is used to prevent the errors that will accure if 2 frames is open at once
            """
        except:
            pass
        #creating the frame that will contain infromation about the room
        self.checkout_frame = tk.Frame(self.root, background=self.white)

        #creating a button that will be closing the information frame
        self.closecheckoutframe_button = tk.Button(self.checkout_frame, command=lambda : self.closecheckoutframe, text="x", fg="red", font=("Arial", 12))
        self.closecheckoutframe_button.pack_forget()

        #a label for the name
        self.checkout_name_label = tk.Label(self.checkout_frame, text="Namn: ", font=("Arial", 13))
        self.checkout_name_label.pack_forget()

        #a label for the emial
        self.checkout_emial_label = tk.Label(self.checkout_frame, text="e-mial: ", font=("Arial", 13))
        self.checkout_emial_label.pack_forget()

        #an entry for the name
        self.checkout_name_entry = tk.Entry(self.checkout_frame)
        #self.checkout_name_entry.pack_forget()

        #an entry for the email
        self.checkout_emial_entry = tk.Entry(self.checkout_frame)
        #self.checkout_emial_entry.pack_forget()

        #a button for continueing the checkout
        self.checkout_go_button = tk.Button(self.checkout_frame, command=self.checkout, text="Fortsätt", bg=self.sky, fg=self.white, font=("Arial", 12))

        #creating the information frame and packing everythin
        self.checkout_frame.place(relx=0.4, rely=0.5)
        self.closecheckoutframe_button.grid(row=0, column=3)
        self.checkout_name_label.grid(row = 1, column=0)
        self.checkout_name_entry.grid(row=1, column=1)
        self.checkout_emial_label.grid(row=2, column=0)
        self.checkout_emial_entry.grid(row=2, column=1)
        self.checkout_go_button.grid(row=3, column =1, sticky=E, pady=20)

    
    def checkout(self):
        """
        this method will get the information that the information that the user 
        gave and match it to a booking, the booking well then be undone
        @return: void
        """
        try:
            self.name = self.checkout_name_entry.get()
            self.mail = self.checkout_emial_entry.get()
        except:
            self.name = ""
            self.mail = ""

        try:
            self.closeinfoframe()
            self.closecheckoutframe()
        except:
            pass

        loginname = self.name
        loginmail = self.mail
        self.checkout_frame.destroy()

        #creating the frame that will contain infromation about the room
        self.information_frame = tk.Frame(self.root, background=self.white)
        self.information_frame.pack_forget()

        #creating the label that will show information about the booked rooms
        self.roominformation_frame = tk.Frame(self.information_frame, background="#E7E0DB")
        self.roominformation_frame.pack_forget()

        #creating a button that will be closing the information frame
        self.closeinfoframe_button = tk.Button(self.information_frame, text="x", command=self.closeinfoframe, fg="red", font=("Arial", 12))

        #creating the information frame and packing everythin
        self.information_frame.place(relx=0.4, rely=0.5)
        self.roominformation_frame.grid(row=1, column=0, columnspan=5, sticky= W)
        self.closeinfoframe_button.grid(row=0, column=5, columnspan=5)

        self.unbook(loginname, loginmail)

    def unbook(self, loginname, loginmail):
        """
        Here, the person will be asked to log in so that their data can be compared
        to the registered users in the text file. 
        @param loginname: the name that will be used to find the right booking to remove
        @param loginmail: the mail-adress that be used to find the right booking to remove
        @retur: void
        """

        with open("SolHotell/people.txt", "r") as people:
            for i, line in enumerate(people.readlines()):
                if line.endswith("\n"):
                    line = line.replace("\n", "")
                if len(line) < 10:
                    continue
                name, mail, street, indate, outdate, id = line.split('|')

                if str(name) == str(loginname) and str(mail) == str(loginmail):
                    with open("SolHotell/bookroom.txt", "r") as booked:
                        for i, room in enumerate(booked.readlines()):
                            if room.endswith("\n"):
                                room = room.replace("\n", "")
                            if str(room[18:21]) == str(id):
                                type = int(room[1:2])
                                rooms = int(room[3:4])
                                beds = int(room[5:6])
                                wifi = int(room[7:8])
                                bld = int(room[9:10])
                                fridge = int(room[11:12])
                                roomid = int(room[13:17])
                                for i in self.bookedrooms:
                                    if roomid == i.roomid:
                                        pass
                                else:
                                    self.remove()
                                    self.bookedrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))

                        for i in self.bookedrooms:
                            i.unbookappear(self.roominformation_frame, type, indate, outdate, id)
    
    
    
    def standard_info(self):
        """
        This method will fetch and show information about the standard rooms
        @return: void
        """
        self.closeRooms()
        self.remove()
        """
        caling methods to close the other rooms-informations
        this will prevent errors since to things can't be shown at 
        once
        """
        for index, i in enumerate(self.standardrooms):
            i.appear(self.roominformation_frame, (index+1), "standard")

    def family_info(self):
        """
        This method will fetch and show information about the family rooms
        @return: void
        """
        #creating and adding a button that will be used for booking a room
        self.closeRooms()
        self.remove()
        """
        caling methods to close the other rooms-informations
        this will prevent errors since to things can't be shown at 
        once
        """
        for index, i in enumerate(self.familyrooms):
            i.appear(self.roominformation_frame, (index+1), "family")

    def deluxe_info(self):
        """
        This method will fetch and show information about the family rooms
        @return: void
        """
        self.closeRooms()
        self.remove()
        """
        caling methods to close the other rooms-informations
        this will prevent errors since to things can't be shown at 
        once
        """
        for index, i in enumerate(self.deluxerooms):
            i.appear(self.roominformation_frame, (index+1), "deluxe")

    def closeinfoframe(self):
        """
        The informationframe will be destroyed and it will be
        created again when the informationbutton is clicked
        @return: void
        """
        self.information_frame.destroy()

    def closecheckoutframe(self):
        """
        The checkoutframe will be destroyed and it will be
        created again when the checkoutbutton is clicked
        @return: void
        """
        self.checkout_frame.destroy()

    def closeRooms(self):
        """
        Method to make sure every previous room is destroyed (not visible) when
        a new tab of rooms is opened.
        """
        try:
            for i in self.standardrooms:
                i.booktext.destroy()
        except:
            pass

        try:
            for i in self.familyrooms:
                i.booktext.destroy()
        except:
            pass

        try:
            for i in self.deluxerooms:
                i.booktext.destroy()
        except:
            pass

    def remove(self):
        """
        Method to update the lists of bookable rooms every time
        the user loads a new tab of bookable rooms. This is important since it makes
        sure that rooms that are already booked don't show up when reloading a tab
        """
        while True:
            for x in self.standardrooms:
                self.standardrooms.remove(x)
            for x in self.deluxerooms:
                self.deluxerooms.remove(x)
            for x in self.familyrooms:
                self.familyrooms.remove(x)
            for x in self.bookedrooms:
                self.bookedrooms.remove(x)

            if self.standardrooms == [] and self.deluxerooms == [] and self.familyrooms == [] and self.bookedrooms == []:
                break

        self.getrooms() #caling the method getrooms so that new rooms are created

#setting 'app' to equal main
app=Main()
#using the run funciton on app
app.run()