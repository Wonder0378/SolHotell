"""
Created by: Samuel Hellqvist and Marcus Hedquist
Date: 09-03-2022
Info:

new file for the hotel
everything is given name like this:

self.what-this-is_what-type-of-tkinter-element-thtis-is
"""

#importar det som programmet behöver 
import tkinter as tk
from tkinter import *
from bookunbook import Room
from random import randint

try:
    from getweather import GetWeather
except: 
    pass
"""
Name: Samuel Hellqvist
Date: 23-03-2022
Info:
This is a weather app that will display what weather it is somewhere in the world
"""

#everything will be udner this main class
class Main():
    def __init__(self):
        self.__roomids = []
        self.getrooms()

        self.title = "Solhotellet, Marcus och Samuel"

        import requests

        #api-nyckeln används för att få tillgång till data om vädret från hela världen
        api_key = '647606470e7d8926da64ece5273d596b'

        #vårat hotell ligger i staden Victoria på Sychellerna och därför är inputen Victoria
        input_ = ("Victoria")

        #data om vädret i Victoria hämtas
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={input_}&units=imperial&APPID={api_key}")

        #variabler sätts
        self.weather = weather_data.json()['weather'][0]['main']
        self.temp = weather_data.json()['main']['temp']

        #variablerna är annars på engelska men översätts här till svenska
        if self.weather == ("Clear"):
            self.weather = ("Klart")
        elif self.weather == ("Clouds"):
            self.weather = ("Molnigt")

        #temperaturen räknas om från fahrenheit till celcius
        self.temp2 = self.temp-32
        self.tempCelcius = round(self.temp2*0.5556)
        self.tempText = str(self.tempCelcius)

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
        self.checkout_button = tk.Button(self.root, text="CHECKA UT", width=20, command=self.checkout, bg=self.carrot, fg=self.white, font="Arial")

        #packing all the tkinter elements and palcing them
        self.header_label.place(relx=0.5, rely=0.17, anchor=CENTER)
        try: 
            self.weather_label.place(relx=0.145, rely=0.3)
        except:
            pass
        self.exit_button.place(relx=0.9, rely=0.9)
        self.roominfo_button.place(relx=0.2, rely=0.5)
        self.checkout_button.place(relx=0.2, rely=0.6)


    def roomid(self):
        while True:
            id = randint(1000, 9999)

            if id in self.__roomids:
                pass
            else:
                break

        return id


    def getrooms(self):
        #Inserting rooms

        self.__standardrooms = []
        self.__deluxerooms = []
        self.__familyrooms = []

        try: # Checks if there are any already registered rooms in the hotel
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

                    if type == 1:
                        self.__standardrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))
                    elif type == 2:
                        self.__deluxerooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))
                    elif type == 3:
                        self.__familyrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))

        
        except: # If file hasn't been created, or is empty, an exception will be made
            for i in range(1, 5): # And 4 rooms of every kind will be created
                self.__standardrooms.append(Room(1, randint(1, 4), randint(2, 4), randint(0, 1), 1, randint(0, 1), self.roomid()))
                self.__deluxerooms.append(Room(2, randint(4, 6), randint(2, 4), 1, randint(2, 4), 1, self.roomid()))
                self.__familyrooms.append(Room(3, randint(3, 5), randint(3, 4), 1, randint(1, 4), randint(0, 1), self.roomid()))

            for i in self.__standardrooms:
                i.register()
            for i in self.__deluxerooms:
                i.register()
            for i in self.__familyrooms:
                i.register()
        

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
        self.roominformation_frame.grid(row=1, column=0, columnspan=5, sticky="w")
        self.closeinfoframe_button.grid(row=0, column=3)

    #function for checkout
    def checkout(self):
        pass
    
    #function for viewing information about the standard room
    def standard_info(self):
        #Placing the rooms
        for index, i in enumerate(self.__standardrooms):
            i.appear(self.roominformation_frame, (index+1), "standard")

        try:
            for i in self.__deluxerooms:
                i.booktext.pack_forget()
            for i in self.__familyrooms:
                i.booktext.pack_forget()
        except:
            pass



    #function for viewing information about the family room
    def family_info(self):
        #creating and adding a button that will be used for booking a room
        for index, i in enumerate(self.__familyrooms):
            i.appear(self.roominformation_frame, (index+1), "family")

        try:
            for i in self.__deluxerooms:
                i.booktext.pack_forget()
            for i in self.__standardrooms:
                i.booktext.pack_forget()
        except:
            pass

    #function for viewing information about the deluxe room
    def deluxe_info(self):
        #opening the file that will contain the information we want to show
        for index, i in enumerate(self.__deluxerooms):
            i.appear(self.roominformation_frame, (index+1), "deluxe")

        try:
            for i in self.__standardrooms:
                i.booktext.pack_forget()
            for i in self.__familyrooms:
                i.booktext.pack_forget()
        except:
            pass

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