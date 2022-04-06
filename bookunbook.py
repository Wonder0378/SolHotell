"""
Created by: Marcus Hedquist
Date: 21-03-22

type = rumstyp (standard, Deluxe, Familjerum)
rooms = antal rum i "rummet"
beds = antal sängar
wifi = 1/0 ja eller nej
bld = frukost/lunch/middag (0 inget, 1 frukost, 2 frukost lunch, 3 allt)
fridge = 1/0 ja eller nej
personid = bokningsid
"""
import tkinter as tk
from tkinter import * 
from random import randint
from tkinter import messagebox as msgbox


class Room:
    
    """
    Klass för att skapa rummen till hotellet
    """
    def __init__(self, type, rooms, beds, wifi, bld, fridge, roomid):
        """
        Konstruktor för att sätta rummets egenskaper
        @param type: typen av rum, från 1-3, standard/deluxe/familj (int)
        @param rooms: mängden rum i "rummet" (int)
        @param beds: mängden sängar i rummet (int)
        @param wifi: sant eller falskt, men kommer representeras av 0 / 1 (int)
        @param bld: se förklaring ovan (int)
        @param fridge: sant eller falskt, 0 / 1 (int)
        @param roomid: Id för rummet (int)
        @return: void
        """
        #färger
        self.carrot = "#ff8e00" #lightest orange
        self.orange = "#fd7702" #medium orange
        self.mandarin = "#ff5003" #darkest orange
        self.sky = "#5b84c4" #lightest blue
        self.blue = "#003f7d" #darkest blue
        self.white = "#ebebeb" #white/grey
        
        self.type = type
        self.rooms = rooms
        self.beds = beds
        self.wifi = wifi
        self.bld = bld
        self.fridge = fridge
        self.roomid = roomid

        self.str_t = "t{}".format(self.type)
        self.str_r = "r{}".format(self.rooms)
        self.str_b = "b{}".format(self.beds)
        self.str_w = "w{}".format(self.wifi)
        self.str_bld = "B{}".format(self.bld)
        self.str_f = "f{}".format(self.fridge)
        self.str_room = "R{}".format(self.roomid)

    def register(self):
        room_open = open('SolHotell/rooms.txt', 'a', encoding='utf-8')

        self.string = self.str_t+self.str_r+self.str_b+self.str_w+self.str_bld+self.str_f+self.str_room

        room_open.write("{}\n".format(self.string))

    def book(self, id):
        file_open = open('SolHotell/bookroom.txt', 'a')

        self.str_id = "i{}".format(id)
        self.string = self.str_t+self.str_r+self.str_b+self.str_w+self.str_bld+self.str_f+self.str_room+self.str_id

        file_open.write("{}\n".format(self.string))
        msgbox.showinfo("Your Room is booked", "Your booking number is: " + str(id))
        self.booktext.pack_forget()
        

    def appear(self, frame, order, type):
        self.booktext = tk.Frame(frame)
        self.booktext.pack(pady=5)

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

        self.front = tk.Label(self.booktext, text=type.upper()+"room".upper(), bg=self.white, font="Arial, 11")
        self.moreinfo = tk.Label(self.booktext,bg=self.white, text="Rooms: {} | Beds: {} | {} | {} | {}".format(self.rooms, self.beds, iswifi, isfridge, bld))
        self.pic = PhotoImage(file="SolHotell/pictures/familjerum.png", width=50, height=50)
        self.bookbtn = tk.Button(self.booktext, text="BOKA", command=lambda : self.book(randint(1, 1000)), bg=self.carrot, fg=self.white, font="Arial, 10", padx=20)
        #self.bookbtn = tk.Button(self.booktext, text="Book")
    
        self.bookbtn.grid(column=5, row=1,)
        self.front.grid(column=0, row=0)
        self.moreinfo.grid(column=0, row=1)
        #self.bookbtn.grid(column=8, row=1, columnspan=2, rowspan=3, sticky="e")
        
        """
        Här kommer rummens utseende
        visas, frame = roominformation_frame
        """