import tkinter as tk
from tkinter import font

Large_Font =("Nunito", 40)
Small_Arial = ("Nunito", 16)
Digit_Font = ("Nunito", 24)
Default_Font = ("Nunito", 20)

glacier = "#CDF0FF"
storm = "#004764"
black = "#000000"
lightblue = "#CCEDFF"
white = "#FFFFFF"
offwhite = "#F8FAFF"

class Calculator:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("SIMPLE CALCULATOR")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits ={
            7:(1, 1),8:(1, 2),9:(1, 3),
            4:(2, 1),5:(2, 2),6:(2, 3),
            1:(3, 1),2:(3, 2),3:(3, 3),
            0:(4, 2),'.':(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    



