
import tkinter as tk
from tkinter import *
from tkinter import Tk, StringVar , ttk


class Converter:
    def __init__(self):     
        self.window = Toplevel()
        self.window.title('UNIT CONVERTER')
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.configure(bg="Black")
        title_label=Label(self.window,text='SELECT CONVERSION:',font = ("Nunito", 20), justify = CENTER, bg="black", fg="white")
        title_label.place(x=40,y=20)

        self.create_menu_buttons()

    def create_menu_buttons(self):
        self.quitbtn = Button(self.window, text="QUIT", bg="gray", fg="white",font = ("Nunito", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.window.destroy)
        self.quitbtn.place(x=160,y=300)
        self.tempbtn = Button(self.window, text="TEMPERATURE", bg="gray" , fg="white",font = ("Nunito", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.TemperatureConverter)
        self.tempbtn.place(x=110,y=120)
        self.lenbtn = Button(self.window, text="LENGTH", bg="gray" , fg="white",font = ("Nunito", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.LengthConverter)
        self.lenbtn.place(x=145,y=180)
        self.weighbtn = Button(self.window, text="WEIGHT", bg="gray" , fg="white",font = ("Nunito", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.WeightConverter)
        self.weighbtn.place(x=145,y=240)

    

