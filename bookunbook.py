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
    def __init__(self, type, rooms, beds, wifi, bld, fridge, roomid):
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

    def book(self, id):
        file_open = open('bookroom.txt', 'w')

        self.str_id = "i{}".format(id)
        self.string = self.str_t+self.str_r+self.str_b+self.str_w+self.str_bld+self.str_f+self.str_room+self.str_id

        file_open.write(self.string)

    def appear(self, frame):
        pass
        """
        Här kommer rummens utseende
        visas, frame = roominformation_frame
        """