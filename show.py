import tkinter
from tkinter import messagebox
import csv
import sys
import search
from functools import partial
from tkinter import ttk
import pandas as pd


def show(file_name): 
        
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
     
    def show_all_data(frame,file_name):
        # open file
        dataset=pd.read_csv(file_name)
        with open(file_name, newline = "") as file:
           reader = csv.reader(file)
        
           # r and c tell us where to grid the labels
           r = 0
           
           for col in reader:
              c = 0
              def details(i,e):
                search.search_id(file_name,str(i))
                print(i)
              for row in col:
                 # i've added some styling
                 if (r==0):
                     label = tkinter.Label(frame, width = 30, height = 2, \
                                       text = row, relief = tkinter.RIDGE, font='arial 10 bold italic')
                 else:
                     label = tkinter.Label(frame, width = 30, height = 2, \
                                       text = row, relief = tkinter.RIDGE,cursor="hand1")
    
                     label.bind("<Button-1>", partial(details,list(dataset[dataset.columns[0]])[r-1]))
                 label.grid(row = r, column = c)
                 c += 1
              r += 1
              
            

    def show_selected_data(file_name,row_no):
        # open file
        for widget in frame.winfo_children():
            widget.destroy()
        
        with open(file_name, newline = "") as file:
           reader = csv.reader(file)
        
           # r and c tell us where to grid the labels
           r = 0
           r1=0
           
           for col in reader:
              c = 0
              def details(i,e):
                search.search_id(file_name,str(i))
              change=0  
              for row in col:
                 # i've added some styling
                 if (r==0):
                     label = tkinter.Label(frame, width = 30, height = 2, \
                                       text = row, relief = tkinter.RIDGE, font='arial 10 bold italic')
                     label.grid(row = r1, column = c)
                     change=1
                 elif r in row_no:
                     label = tkinter.Label(frame, width = 30, height = 2, \
                                       text = row, relief = tkinter.RIDGE,cursor="hand1")
    
                     label.bind("<Button-1>", partial(details,list(dataset[dataset.columns[0]])[r-1]))
                     label.grid(row = r1, column = c)
                     change=1
                 else:
                    change=0
                 c += 1
              r+=1
              if change==1:
                 r1 += 1
            
        
        
    
    def search_data():
        if combo_Search.get()=='':
            messagebox.showerror("Error", "Enter an attribute...")
        else:
            dataset=pd.read_csv(file_name)
            row_no=[]
            flag=1
            for i in list(dataset[combo_Search.get()]):
                if str(i)==combo_Search1.get():
                    row_no.append(flag)
                flag+=1
            print(row_no)
            show_selected_data(file_name,row_no)
    def show_all():
        for widget in frame.winfo_children():
            widget.destroy()
        show_all_data(frame,file_name)
        
    root = tkinter.Toplevel()
    root.title("DataBase")
    root.resizable(False,False)
    
    screen_width = root.winfo_screenwidth()-20
    screen_height = root.winfo_screenheight()-50
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()-35
    root.geometry("%dx%d+0+0" % (w, h))
    #root.resizable(0,0)
    if ( sys.platform.startswith('win')): 
        root.iconbitmap('icon/task.ico')
    else:
        photo = tkinter.PhotoImage(file = "icon/task.gif")
        root.iconphoto(False, photo)
    
    
    lbl_Search=tkinter.Label(root,text="Search By",bg="lightsteelblue",fg="white",font=("times new roman",20,"bold"))
    lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
    
    dataset=pd.read_csv(file_name)

    combo_Search1=ttk.Combobox(root,width=20,font=("times new roman",13),state='readonly')
    combo_Search1['values']=()
    def callback(event=None):
        value=list(dict.fromkeys(dataset[event.widget.get()]))
        value.sort()
        combo_Search1['values']=value
        combo_Search1.current(0)
    
    combo_Search=ttk.Combobox(root,width=20,font=("times new roman",13),state='readonly')
    combo_Search['values']=sorted(dataset)
    combo_Search.grid(row=0,column=1,pady=20,padx=10)
    combo_Search.bind('<<ComboboxSelected>>',callback)

    
    
    combo_Search1.grid(row=0,column=2,pady=20,padx=10)
    
    
    Searchbtn=tkinter.Button(root,text="Search",width=10,pady=5,command=search_data).grid(row=0,column=3,padx=10,pady=10)
    Showallbtn=tkinter.Button(root,text="Show All",width=10,pady=5,command=show_all).grid(row=0,column=4,padx=10,pady=10)

    
    
    Table_Frame=tkinter.Frame(root,bd=4,relief=tkinter.RIDGE,bg="lightsteelblue")
    Table_Frame.place(x=20,y=80,width=screen_width-30,height=screen_height-80)

    canvas = tkinter.Canvas(Table_Frame)
    canvas.place(width = screen_width-50,height = screen_height-100)
    scrollbar = tkinter.Scrollbar(Table_Frame, command=canvas.yview)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    canvas.configure(yscrollcommand = scrollbar.set)
    
    scrollbarV = tkinter.Scrollbar(Table_Frame, command=canvas.xview,orient=tkinter.HORIZONTAL)
    scrollbarV.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.configure(xscrollcommand = scrollbarV.set)
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', on_configure)
    frame = tkinter.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    
    show_all_data(frame,file_name)
    
