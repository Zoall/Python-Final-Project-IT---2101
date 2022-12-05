
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
        
    def WeightConverter(self):
        self.factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
        self.ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "Gram" : 'g', "Centigram" : 'cg', "Milligram" : 'mg'}
        
        self.weigh_window = Toplevel()
        self.weigh_window.title("Weight Converter")
        self.weigh_window.geometry("375x667")
        self.weigh_window.resizable(False, False)
        
        self.weigh_frame = tk.Frame(self.weigh_window, bg="black")
        self.weigh_frame.pack(fill=BOTH, expand=1)
        self.titleLabel = Label (self.weigh_frame, text = "WEIGHT CONVERSION", font = ("Nunito", 20), justify = CENTER, bg = "black", fg="white")
        self.titleLabel.grid(column=1,row=1)

        self.in_amt = StringVar()
        self.in_amt.set('0')
        self.out_amt = StringVar()

        self.in_unit = StringVar()
        self.out_unit = StringVar()
        self.in_unit.set('Select Unit')
        self.out_unit.set('Select Unit')

        self.in_field = ttk.Entry(self.weigh_frame, width=20, textvariable=self.in_amt, font=("Nunito", 20))
        self.in_field.grid(row=3, column=1, sticky=(W, E))


        self.in_select = OptionMenu(self.weigh_frame, self.in_unit, "Kilogram","Hectagram","Decagram", "Gram", "Decigram","Centigram", "Milligram")
        self.in_select.config(width=10, height = 3, bg="black", font=("Nunito", 10, "bold"), fg="white") 
        self.in_select.grid(column=1, row=2, sticky=W)

        self.txtLabel = Label(self.weigh_frame, text = "Convert To:", font= ("Nunito", 13, "bold"), bg = "black", fg="white")
        self.txtLabel.grid(row = 4, column = 1)

        def convert(amt, frm, to):
            if frm != 'g':
                amt = amt * self.factors[frm]
                return amt / self.factors[to]
            else:
                return amt / self.factors[to]

        def callback():
            try:
                amt = float(self.in_field.get())
            except ValueError:
                self.out_amt.set('Invalid input')
                return None
            if self.in_unit.get() == 'Select Unit' or self.out_unit.get() == 'Select Unit':
                self.out_amt.set('Input or output unit not chosen')
                return None
            else:
                frm = self.ids[self.in_unit.get()]
                to = self.ids[self.out_unit.get()]
                self.out_amt.set(convert(amt, frm, to))
      
    
        self.out_field = ttk.Entry(self.weigh_frame, textvariable=self.out_amt, state="readonly", font=("Nunito", 20))
        self.out_field.grid(column=1, row=6, sticky=(W, E))
        self.in_select = OptionMenu(self.weigh_frame, self.out_unit, "Kilogram","Hectagram","Decagram", "Gram", "Decigram","Centigram", "Milligram")
        self.in_select.config(width=10, height = 3, bg="black", font=("Nunito", 10, "bold"), fg="white")
        self.in_select.grid(column=1, row=5, sticky=W)

        self.conv_button = tk.Button(self.weigh_frame, text="CONVERT", font=("Nunito", 10, "bold"), activebackground="green", activeforeground="white", command=callback)
        self.conv_button.grid(column=1, row=7, sticky=W, ipadx = 10, ipady = 10)

        for child in self.weigh_frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.in_field.focus()
        
   def LengthConverter(self):
        
        self.factors = {'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
        self.ids = {"Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "Meters" : 'm', "Centimeters" : 'cm', "Millileters" : 'mm'}

        self.len_window = Toplevel()
        self.len_window.title("Length Converter")
        self.len_window.geometry("375x667")
        self.len_window.resizable(False, False)

        self.len_frame = tk.Frame(self.len_window, bg="black")
        self.len_frame.pack(fill=BOTH, expand=1)
        self.titleLabel = Label (self.len_frame, text = "LENGTH CONVERSION", font = ("Nunito", 20), justify = CENTER, bg = "black", fg ="white")
        self.titleLabel.grid(column=1,row=1)

        self.in_amt = StringVar()
        self.in_amt.set('0')
        self.out_amt = StringVar()

        self.in_unit = StringVar()
        self.out_unit = StringVar()
        self.in_unit.set('Select Unit')
        self.out_unit.set('Select Unit')

        self.in_field = ttk.Entry(self.len_frame, width=20, textvariable=self.in_amt, font=("Nunito",20))
        self.in_field.grid(row=3, column=1, sticky=(W, E))

        self.in_select = OptionMenu(self.len_frame, self.in_unit, "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters", "Millileters")
        self.in_select.config(width=10, height = 3, bg="black", font=("Nunito", 10, "bold"), fg="white") 
        self.in_select.grid(column=1, row=2, sticky=W)

        self.txtLabel = Label(self.len_frame, text = "Convert To:", font= ("Nunito", 13, "bold"), bg = "black", fg="white")
        self.txtLabel.grid(row = 4, column = 1)


        def convert(amt, frm, to):
            if frm != 'm':
                amt = amt * self.factors[frm]
                return amt / self.factors[to]
            else:
                return amt / self.factors[to]

        def callback():
            try:
                amt = float(self.in_field.get())
            except ValueError:
                self.out_amt.set('Invalid input')
                return None
            if self.in_unit.get() == 'Select Unit' or self.out_unit.get() == 'Select Unit':
                self.out_amt.set('Input or output unit not chosen')
                return None
            else:
                frm = self.ids[self.in_unit.get()]
                to = self.ids[self.out_unit.get()]
                self.out_amt.set(convert(amt, frm, to))

       
 
        self.out_field = ttk.Entry(self.len_frame, textvariable=self.out_amt, state="readonly", font=("Nunito",20))
        self.out_field.grid(column=1, row=6, sticky=(W, E))
        self.in_select = OptionMenu(self.len_frame, self.out_unit, "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters", "Millileters")
        self.in_select.config(width=10, height = 3, bg="black", font=("Nunito", 10, "bold"), fg="white")
        self.in_select.grid(column=1, row=5, sticky=W)

        self.conv_button = tk.Button(self.len_frame, text="CONVERT", font=("Nunito", 10, "bold"), activebackground="green", activeforeground="white", command=callback)
        self.conv_button.grid(column=1, row=7, sticky=W, ipadx = 10, ipady = 10)

        for child in self.len_frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.in_field.focus()


    

