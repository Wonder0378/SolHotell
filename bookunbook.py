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
        file_open = open('../bookroom.txt', 'a')

        self.str_id = "i{}".format(id)
        self.string = self.str_t+self.str_r+self.str_b+self.str_w+self.str_bld+self.str_f+self.str_room+self.str_id

        file_open.write("{}\n".format(self.string))

    def appear(self, frame, order):
        self.booktext = tk.Frame(frame)
        self.booktext.grid(column=1, row=order, columnspan=4, pady=10)

        self.front = tk.Label(self.booktext, text="Room {}, type {}".format(order, self.type))
        self.moreinfo = tk.Label(self.booktext, text="Rooms: {} | Beds: {}".format(self.rooms, self.beds))
        self.front.grid(column=1, row=1)
        self.moreinfo.grid(column=1, row=2)
        """
        Här kommer rummens utseende
        visas, frame = roominformation_frame
        """