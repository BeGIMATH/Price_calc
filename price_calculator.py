
"""In this journey we are going to try to write a complete GUI for a program which does the recommendation to useers
"""
import tkinter as tk #Import the main library 
win = tk.Tk() #Create an instance of the class Tk by calling its constructor
win.title('Ticket price calculator') #Write the title of the window

#Adding a label widget
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *

#Creating menu bars

#First import the menu class from tkinter
from tkinter import Menu

def _quit():
    win.quit()
    win.destroy()
    exit()

menuBar = Menu(win)
win.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File",menu=fileMenu)
#Adding a separator line between the menuitems
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)



#Creating message boxes
from tkinter import messagebox as mBox 
# Create a callback function which  displays the messagebox
def _msgBox():
    mBox.showinfo('Python Message Info Box', ' A python GUI created using tkinter:\nThe year is 2015')
    #mBox.showwarning('Python Message Warning Box',' A python GUI created using tkinter:\nWarning: There might be a bug in this code')
# Add anothe Menu to the menubar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About",command=_msgBox)
menuBar.add_cascade(label="Help",menu=helpMenu)


#we are creating a container frame to hold all other widgets



#Adding a text box widget
win1 = ttk.LabelFrame(win,text="Train Ticket Price Calculator")
win1.grid(column=0,row=0,sticky="nsew")
#ttk.Label(win1,text="Please choose two cities!").grid(column=0,row=0,sticky=tk.W)
#Adding a textbox entry widget

#Combo box widgets
ttk.Label(win1, text="Origin:").grid(column=0, row=1)
number1 = tk.StringVar()
initial = ttk.Combobox(win1,width=12, textvariable=number1,state='readonly')
initial['values'] = ('MADRID','SEVILLA','PONFERRANDA','BARCELONA','VALENCIA')
initial.grid(column=1,row=1,padx=10,pady=10)
initial.current(0)

ttk.Label(win1, text="Destination:").grid(column=0, row=2)
number2 = tk.StringVar()
destination = ttk.Combobox(win1,width=12, textvariable=number2,state='readonly')
destination['values'] = ('MADRID','SEVILLA','PONFERRANDA','BARCELONA','VALENCIA')
destination.grid(column=1,row=2, padx=10,pady=10)
destination.current(0)


ttk.Label(win1, text="Class:").grid(column=0, row=3)
number3 = tk.StringVar()
classs = ttk.Combobox(win1,width=12, textvariable=number3,state='readonly')
classs['values'] = ('Turista','Preferente','Turista Plus','Turista con enlace')
classs.grid(column=1,row=3, padx=10,pady=10)
classs.current(0)





win2 = ttk.LabelFrame(win)
win2.grid(column=0,row=1, sticky="nsew")

win3 = ttk.LabelFrame(win)
win3.grid(column=0,row=2, sticky="nsew")



def dateentry_view():
    def print_sel():
        print(cal.get_date())
    
    def show_price():
        top = tk.Toplevel(win)
        
        width = 500
        height = 400
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        top.geometry("%dx%d+%d+%d" % (width, height, x, y))
        top.resizable(True,True)

        TableMargin = Frame(top, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Origine", "Destination", "Start_date", "End_date", "Price", "Class"), height=200, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Origine', text="Origine", anchor=W)
        tree.heading('Destination', text="Destination", anchor=W)
        tree.heading('Start_date', text="Start date", anchor=W)
        tree.heading('End_date', text="End date", anchor=W)
        tree.heading('Price', text="Price", anchor=W)
        tree.heading('Class', text="Class", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=300)
        tree.column('#4', stretch=NO, minwidth=0, width=300)
        tree.column('#5', stretch=NO, minwidth=0, width=300)
        tree.column('#6', stretch=NO, minwidth=0, width=300)
        tree.pack()

        with open('Tickets.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader: 
                Origine = row['origin']
                Destination = row['destination']
                Start_date = row['start_date']
                End_date = row['end_date']
                Price = row['price']
                Class = row['train_class']
                if Origine == initial.get() and Destination == destination.get() and Class == classs.get() and str(cal.get_date()) in  str(Start_date) and number4.get() in str(Start_date):
                    tree.insert("", 0, values=(Origine, Destination, Start_date, End_date, Price, Class))


    
    cal = DateEntry(win3, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.grid(column=1,row=3,padx=10, pady=10)
    cal.bind("<<DateEntrySelected>>", print_sel())
    ttk.Button(win3, text="Confirm", command=print_sel).grid(column=0,row=0)
    ttk.Button(win3,text="Price!", command=show_price).grid(column=1,row=0)
    ttk.Label(win3, text="Time").grid(column=0,row=2,padx=10,pady=10)
    number4 = tk.StringVar()
    hour = ttk.Entry(win4,textvariable=number4, width=2)
    hour.grid(column=0,row=3)
    ttk.Label(win4, text="/").grid(column=1,row=3)
    number5 = tk.StringVar()
    Min = ttk.Entry(win4,textvariable=number5,width=2).grid(column=2,row=3)
    
ttk.Button(win2, text='Date', command=dateentry_view).grid(column=0,row=0,padx=10, pady=10)



import csv
win3 = ttk.LabelFrame(win)
win3.grid(column=0,row=2, sticky="nsew")
   
win4 = ttk.LabelFrame(win3)
win4.grid(column=0,row=3,sticky="N")

win.mainloop() #Without this part the window will not appear

