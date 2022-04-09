#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:35:01 2020

@author: jenar
"""



import tkinter
from tkinter import messagebox
import csv



def edit_id(file,id):
    row_no=0
    with open(file, "r",newline = "") as f:
        reader = csv.reader(f)
        for line_num, content in enumerate(reader):
            if content[0] == id:
                row_no=line_num
    
    def cancel():
        root.destroy()
    def edit():
        c=0
        for i in entries:
            if c!=0:
                i.config(state=tkinter.NORMAL)
            c+=1
    def save():
        response=[]
        for en in entries:
            response.append(en.get("1.0",'end-1c'))
        print(response)
        MsgBox = messagebox.askquestion ('Save Database','Once changes are made it is impossible to retrive the old data',icon = 'warning')
        if MsgBox == 'yes':
            print("save")
        print("dc")
    root = tkinter.Tk()
    root.title("EDit db")
    width = 450
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.configure(background="#B3B3B3")
    root.resizable(0,0)
    
    photo = tkinter.PhotoImage(file = "icon/task.gif")
    root.iconphoto(False, photo)
    
    
    
    entries=[]
    r = 0 
    # open file
    with open(file, newline = "") as file:
       reader = csv.reader(file)
    
       # r and c tell us where to grid the labels
       
       for col in reader:
          c = 0
          for row in col:
             # i've added some styling
             if (r==0):
                 tkinter.Label(root, width = 40, height = 2, \
                                   text = row, relief = tkinter.RIDGE, font='arial 10 bold italic', anchor='w').grid(row = c+1, column = 1,pady=3,padx=5)
             
             if (r==row_no):
                 en=tkinter.Text(root, width = 20, height = 1.5,\
                                    relief = tkinter.RIDGE,font='arial 9 ',undo=True)
                 en.grid(row = c+1, column = 2,pady=3,padx=1)
                 en.insert(tkinter.INSERT,row)
                 en.config(state=tkinter.DISABLED)
                 entries.append(en)
             c += 1
          r += 1
    tkinter.Button(root, text='Cancel',font='arial 10 bold italic', cursor="hand1",height=2,width=6, command=cancel).place(relx = 0.62, rely = 0.98, anchor = tkinter.SE) 
    tkinter.Button(root, text='Edit',font='arial 10 bold italic', cursor="hand1",height=2,width=5, command=edit).place(relx = 0.8, rely = 0.98, anchor = tkinter.SE)
    tkinter.Button(root, text='Save',font='arial 10 bold italic',cursor="hand1",height=2,width=5, command=save).place(relx = 0.979, rely = 0.98, anchor = tkinter.SE)

    if row_no==0:
        messagebox.showerror("Error", "Enter a valid Team id...")
        root.destroy()
        
    root.mainloop()
#edit_id("test.csv","5")