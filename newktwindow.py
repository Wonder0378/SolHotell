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
from getweather import GetWeather
from random import randint
"""
Name: Samuel Hellqvist
Date: 23-03-2022
Info:
This is a weather app that will display what weather it is somewhere in the world
"""

#hela programmet kommer att skriva under denna main class
class Main():
    def __init__(self):
        self.__roomids = []
        self.getrooms()

        self.title = "Solhotellet, Marcus och Samuel"
        weather = GetWeather()

        #root, där alltig kommer sättas
        self.root = tk.Tk()

        #sätter pic till en bild
        self.pic = PhotoImage(file="SolHotell/pictures/finstrand.png")

        #sätter olika frägvariabler som kommer att användas senare
        self.carrot = "#ff8e00" #lightest orange
        self.orange = "#fd7702" #medium orange
        self.mandarin = "#ff5003" #darkest orange

        self.sky = "#5b84c4" #lightest blue
        self.blue = "#003f7d" #darkest blue

        self.white = "#ebebeb" #white/grey

        #text variabel
        self.text = tk.StringVar()
        self.text.set("")

        #sätter skärmen till fullskärm
        self.root.attributes("-fullscreen", True)

        #sätter en label som blir bakgrundsbilden
        self.bg_label = tk.Label(self.root, image=self.pic)
        self.bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        #skapar en headline
        self.header_label = tk.Label(self.root, text="☀" + "SAMMYS" + " "*3 + "SOLHOTELL" + "☀", bg=self.blue, fg=self.carrot, font=("Broadway", 50))

        #skapar en widget där hotellets nuvarande väder skrivs ut
        self.weather_label = tk.Label(self.root, text="Vädret på hotellet just nu: \n" + weather.tempText + "°C" + "\n" + weather.weather, bg=self.sky, fg=self.white, font=("Arial, 11"))

        #skapar en exit-knapp som kommer ha command self.escape
        self.exit_button = tk.Button(self.root, text="EXIT", command=self.escape, width=10, bg=self.carrot, fg="black")

        #skapar en knapp som visar alla rum
        self.roominfo_button = tk.Button(self.root, text="CHECKA IN", width=20, command=self.view, bg=self.carrot, fg=self.white, font="Arial")

        #skapar en knapp som kommer användas när man vill chekca ut
        self.checkout_button = tk.Button(self.root, text="CHECKA UT", width=20, command=self.checkout, bg=self.carrot, fg=self.white, font="Arial")

        #placerar alla tkinter element
        self.header_label.place(relx=0.5, rely=0.17, anchor=CENTER)
        self.weather_label.place(relx=0.145, rely=0.3)
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

                    if type == 1:
                        self.__standardrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))
                    elif type == 2:
                        self.__deluxerooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))
                    elif type == 3:
                        self.__familyrooms.append(Room(type, rooms, beds, wifi, bld, fridge, roomid))

        
        except:
            for i in range(1, 5):
                self.__standardrooms.append(Room(1, randint(1, 4), randint(2, 4), randint(0, 1), 1, randint(0, 1), self.roomid()))
                self.__deluxerooms.append(Room(2, randint(4, 6), randint(2, 4), 1, randint(2, 4), 1, self.roomid()))
                self.__familyrooms.append(Room(3, randint(3, 5), randint(3, 4), 1, randint(1, 4), randint(0, 1), self.roomid()))

            for i in self.__standardrooms:
                i.register()
            for i in self.__deluxerooms:
                i.register()
            for i in self.__familyrooms:
                i.register()
        

    #funktion som gör att programmet körs
    def run(self):
        self.root.mainloop()

    #funktion som stänger programmet genom att ta bort rooten
    def escape(self):
        self.root.destroy()

    #funktion för att se alla rummen
    def view(self):
        #skapar en frames
        self.information_frame = tk.Frame(self.root, background=self.white)
        self.roominformation_frame = tk.Frame(self.information_frame, background="#E7E0DB")

        #en knapp som kommer att visa information om standard-rummet
        self.economyroom_info_button = tk.Button(self.information_frame, text="Standardrum", command=self.standard_info, padx=30, font=("Arial", 12), bg=self.sky, fg=self.white)
        self.economyroom_info_button.pack_forget()

        #en knapp som kommer att visa information om lyx-rummet
        self.deluxeroom_info_button = tk.Button(self.information_frame, text="Deluxerum", command=self.deluxe_info, padx=30, font=("Arial", 12), bg=self.sky, fg=self.white)
        #this bit of code lets ut hide the button until we need it
        self.deluxeroom_info_button.pack_forget()
        
        #en knapp som kommer att visa information om familje-rummet
        self.familyroom_info_button = tk.Button(self.information_frame, text="Familjerum", command=self.family_info, padx=30, font=("Arial", 12), bg=self.sky, fg=self.white)
        self.familyroom_info_button.pack_forget()

        #en knapp som stänger new informations-rutan
        self.closeinfoframe_button = tk.Button(self.information_frame, text="x", command=self.closeinfoframe, fg="red", font=("Arial", 12))
        self.closeinfoframe_button.pack_forget()

        #packar och placerar alla emelent
        self.information_frame.place(relx=0.4, rely=0.5)
        self.economyroom_info_button.grid(row=0, column=0)
        self.deluxeroom_info_button.grid(row=0, column=1)
        self.familyroom_info_button.grid(row=0, column=2)
        self.text.set( "\n Klicka på någon av knapparna för att få information om det rummet \n")
        self.roominformation_frame.grid(row=1, column=0, columnspan=5, sticky="w")
        self.closeinfoframe_button.grid(row=0, column=3)

    #checka-ut funktion
    def checkout(self):
        pass
    
    #funktion för att visa information om standard-rummet
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



    #funktion för att visa information om familje-rummet
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

    #funktion för att visa information om lyx-rummet
    def deluxe_info(self):
        for index, i in enumerate(self.__deluxerooms):
            i.appear(self.roominformation_frame, (index+1), "deluxe")

        try:
            for i in self.__standardrooms:
                i.booktext.pack_forget()
            for i in self.__familyrooms:
                i.booktext.pack_forget()
        except:
            pass

    #funktion som kommer att stänga informations-rutan
    def closeinfoframe(self):
        self.information_frame.destroy()

    #funktion för att boka ett rum
    def bookroom(self):
        pass

#kör tkinter-förnstret
app=Main()
app.run()