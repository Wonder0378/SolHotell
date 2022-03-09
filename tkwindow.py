"""
Name: Samuel Hellqvist
Date: 18-02-2022
Info:
<Insert information about file>
"""

from tkinter import *
import tkinter.messagebox as msgbox
root=Tk()
from turtle import *
class Main:
    root.wm_attributes('-transparentcolor', 'grey')
    #sets the variable pic to the name of a picture in the direcotry
    pic = PhotoImage(file="SolHotell/pictures/finstrand.png")

    def view():
        pass

    def disable_event():
        pass

    #function that shuts the program off, the exit button will be using this function
    def escape():

        #shutting down the program by destrying the tk window
        root.destroy()

        #sending a goodbye message via turtle
        #preperation
        hideturtle()
        width(7)
        speed(0)
        bgcolor("medium blue")
        pencolor("gold")
        up()
        backward(250)
        left(90)
        forward(100)
        left(180)
        
        #drawing the letter H
        down()
        forward(150)
        left(180)
        forward(75)
        right(90)
        forward(75)
        left(90)
        forward(75)
        left(180)
        forward(150)
        
        #move
        up()
        left(90)
        forward(20)
        left(90)
        forward(37.5)
        right(90)
        down()
        
        #drawing the letter E
        forward(75)
        left(90)
        forward(37.5)
        left(90)
        forward(75)
        left(90)
        forward(75)
        left(90)
        forward(75)
        
        #move
        up()
        forward(20)
        left(90)
        forward(75)
        left(180)
        down()
        
        #drawing the letter J
        forward(150)
        right(90)
        forward(37.5)
        right(90)
        forward(20)
        up()
        forward(160)
        right(90)
        forward(37.5)
        right(90)
        down()
        forward(10)
        
        #move
        up()
        forward(100)
        left(90)
        forward(95)
        left(90)
        down()
        
        #drawing the letter D
        forward(150)
        left(180)
        forward(75)
        right(90)
        forward(75)
        left(90)
        forward(75)
        left(90)
        forward(75)
        
        #move
        up()
        forward(95)
        left(90)
        down()
        
        #drawing the letter  Å
        forward(75)
        left(90)
        forward(75)
        left(90)
        forward(75)
        left(90)
        forward(100)
        up()
        left(90)
        forward(100)
        left(90)
        forward(45)
        down()
        forward(25)
        right(90)
        forward(10)
        right(90)
        forward(25)
        right(90)
        forward(10)
        
        #move
        up()
        left(90)
        forward(45)
        right(90)
        forward(120)
        right(90)
        down()
        
        # drawing an underline
        forward(200)
        up()
        forward(30)
        down()
        
        forward(180)
        right(90)
        
        #move
        up()
        left(180)
        forward(50)
        left(90)
        forward(210)
        
        #write välkommen åter
        pencolor('gold')
        style = ('Brush Script MT', 30, 'italic')
        write('Välkommen åter!', font=style)
        
        #move
        left(90)
        forward(300)
        
        #write sammy's solhotell
        #turtle.color('orange')
        #style = ('Arial', 30,)
        #turtle.write('SAMMMYS SOLHOTELL', font=style, align=CENTER)
        
        done()


    #root.geometry("992x450")

    #makes the tk window fullscreen
    root.attributes("-fullscreen", True)

    #sets the background image to pic
    my_label=Label(root, image=pic)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)

    #creates the headline
    my_headline = Label(root, text="☀" + "Sammy's" + " "*3 + "solhotell" + "☀",fg="orange", font=("Broadway", 50), bg='medium blue')
    my_headline.place(relx=0.5, rely=.3, anchor=CENTER)
    
    #creates the exit button, the button uses the command escape
    my_button = Button(root, text="exit", command=escape, fg="red", width=10)
    my_button.place(relx=0.9, rely=0.9)

    #creates the view our rooms button
    my_rooms = Button(root, text="UPPTÄCK VÅRA RUM", width=20, command=view, bg="orange", fg="white", font="Arial")
    my_rooms.place(relx=0.2, rely=0.5)

    #creates the check out button
    my_checkout = Button(root, text="CHECKA UT", width=20, command="checkout", bg="orange", fg="white", font="Arial")
    my_checkout.place(relx=0.2, rely=0.6)

    new_label = Label(root)
    new_label.place(relx=0.3, rely=0.5)
    #root.protocol("WM_DELETEWINDOW", disable_event)

root.mainloop()