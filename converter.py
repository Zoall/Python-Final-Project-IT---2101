
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
        
   def TemperatureConverter(self):
        def convert():
            celTemp = celTempVar.get()
            fahTemp = fahTempVar.get()
            kelTemp = kelTempVar.get()

            if celTempVar.get() != 0.0:
                celToFah = (celTemp *  9/5 + 32)
                celToKel = (celTemp - 273.15)
                fahTempVar.set(celToFah)
                kelTempVar.set(celToKel)

            elif fahTempVar.get() != 0.0:
                fahToCel = ((fahTemp - 32) * (5/9))
                fahToKel = ((fahTemp - 32) * (5/9) + 273.15)
                celTempVar.set(fahToCel)
                kelTempVar.set(fahToKel)

            elif kelTempVar.get() != 0.0:
                kelToCel = (kelTemp + 273.15)
                kelToFah = ((kelTemp - 273.15) * 9/5 + 32)
                celTempVar.set(kelToCel)
                fahTempVar.set(kelToFah)

        def reset():
            top = Toplevel(padx=50, pady=50)
            top.grid()
            message = Label(top, text = "Reset Complete")
            button = Button(top, text="OK", command=top.destroy)

            message.grid(row = 0, padx = 5, pady = 5)
            button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

            fahTempVar.set(int(0))
            celTempVar.set(int(0))
            kelTempVar.set(int(0))

        top = Toplevel()
        top.title("TEMPERATURE CONVERTER")
        top.geometry("375x667")
        top.resizable(False, False)
        top.configure(bg="black")

        celTempVar = IntVar()
        celTempVar.set(int(0))
        fahTempVar = IntVar()
        fahTempVar.set(int(0))
        kelTempVar = IntVar()
        kelTempVar.set(int(0))

        titleLabel = Label (top, text = "TEMPERATURE CONVERSION", font = ("Nunito",18 ), justify = CENTER, bg = "black", fg = "white")
        titleLabel.grid(column=1,row=1)
        

        celLabel = Label (top, text = "CELCIUS: ", font = ("Nunito", 16), bg="black", fg = "white")
        celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)
        
        fahLabel = Label (top, text = "FAHRENHEIT: ", font = ("Nunito", 16), bg="black", fg = "white")
        fahLabel.grid(row = 4, column = 1, pady = 10, sticky = NW)

        kelLabel = Label (top, text = "KELVIN: ", font = ("Nunito", 16), bg="black", fg = "white")
        kelLabel.grid(row = 6, column = 1, pady = 10, sticky = NW)

        celEntry = Entry (top, font = ("Nunito", 15), width = 20, bd = 5, textvariable = celTempVar)
        celEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 50 )

        fahEntry = Entry (top, font = ("Nunito", 15), width = 20, bd = 5, textvariable = fahTempVar)
        fahEntry.grid(row = 5, column = 1, pady = 10, sticky = NW, padx = 50 )

        kelEntry = Entry (top, font = ("Nunito", 15), width = 20, bd = 5, textvariable = kelTempVar)
        kelEntry.grid(row = 7, column = 1, pady = 10, sticky = NW, padx = 50 )

        celSym = Label(top, text ="°C", font = ("Nunito", 16), bg="black", fg="white")
        celSym.grid(row = 3, column = 2, pady = 10, sticky = NW)

        fahSym = Label(top, text ="°F", font = ("Nunito", 16), bg="black", fg="white")
        fahSym.grid(row = 5, column = 2, pady = 10, sticky = NW)

        kelSym = Label(top, text ="°K", font = ("Nunito", 16), bg="black", fg="white")
        kelSym.grid(row = 7, column = 2, pady = 10, sticky = NW)

        convertButton =Button (top, text = "CONVERT", font = ("Nunito", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command = convert)
        convertButton.grid(row = 8, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx= 20)

        resetButton = Button (top, text = "RESET", font = ("Nunito", 8, "bold"), relief = RAISED, bd=5, justify = CENTER,  overrelief = GROOVE, activebackground = "red", activeforeground="white", command = reset)
        resetButton.grid(row = 9, column = 1,ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 20)


    

