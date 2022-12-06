import tkinter as tk

from tkinter import *
from utils.notepad import *
from utils.calcu import *
from utils.converter import *


class App:
    def __init__(self):     
        self.window = Tk()
        self.window.title('ALL IN ONE APPLICATION')
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.configure(bg="Black")
        title_label=tk.Label(self.window,text='SELECT A FEATURE:',font = ("Nunito", 20, "bold"), justify = CENTER, bg="black", fg="white")
        title_label.place(x=50,y=20)

        self.create_main_ui_buttons()

    def create_main_ui_buttons(self):    
        self.calcbtn = Button(self.window, text="CALCULATOR", bg="gray" , fg="white",font = ("Nunito", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command=Calculator)
        self.calcbtn.place(x=85,y=120)
        self.convbtn = Button(self.window, text="CONVERTER", bg="gray" , fg="white",font = ("Nunito", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command=Converter)
        self.convbtn.place(x=95,y=200)
        self.notebtn = Button(self.window, text="NOTE PAD", bg="gray" , fg="white",font = ("Nunito", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command=Notepad)
        self.notebtn.place(x=110,y=280)
        self.exitbtn = Button(self.window, text="EXIT", bg="gray", fg="white",font = ("Nunito", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "red", activeforeground="white", command=self.window.destroy)
        self.exitbtn.place(x=150,y=360)

    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

