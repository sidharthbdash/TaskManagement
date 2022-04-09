#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 05:03:15 2020

@author: jenar
"""



import tkinter
from tkinter import messagebox
import csv
from csv import writer
import pandas as pd
import show
 
def append_list_as_row(file_name, list_of_elem):
    print(file_name,list_of_elem)
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def warning(warn):
     messagebox.showwarning("Warning", warn)
     
#validtion is not dynamic
def validate(response,file_name):
    dataset=pd.read_csv(file_name)
    attributes=dataset.columns
    for i in range(len(attributes)):
        if response[i]=="":
            warn="Enter "+attributes[i]
            warning(warn)
            return True
        elif i==0:
            if response[0] in list(dataset[attributes[0]]):
                warning('"'+attributes[0]+'" already Present')
                return True
    for i in range(5):
        if  not response[i].isdigit():
            warning('"'+attributes[i]+'" should be a number')
            return True
    for i in range(5,7):
        if response[i] not in ['High','Medium','Low']:
            warning('"'+attributes[i]+'" should be either High, Medium or Low')
            return True
    
    if  not response[7].isdigit():
        warning('"'+attributes[7]+'" should be a number')
        return True
        
    for i in range(8,11):
        if response[i] not in ['1','2','3']:
            warning('"'+attributes[i]+'" should be either 1, 2 or 3')
            return True
def add_team(file_name):
    def cancel():
        root.destroy()
 
    def save():
        response=[]
        for en in entries:
            response.append(en.get("1.0",'end-1c').strip())
            
        for i in range(5,7):
            response[i]=response[i][0].upper()+response[i][1:].lower()
        print(response)
        if validate(response,file_name):
            return
        MsgBox = messagebox.askquestion ('Add Database','Once changes are made it is impossible to retrive the old data',icon = 'warning')
        if MsgBox == 'yes':
            append_list_as_row(file_name, response)
            MsgBox1 = messagebox.askquestion ('Data saved successfully','Do you want to open the employee database',icon = 'question')
            if MsgBox1 == 'yes':
                show.show(file_name)
    root = tkinter.Toplevel()
    root.title("Add Team")
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
    with open(file_name, newline = "") as file:
       reader = csv.reader(file)
    
       # r and c tell us where to grid the labels
       
       for col in reader:
          c = 0
          for row in col:
             # i've added some styling
             if (r==0):
                 tkinter.Label(root, width = 40, height = 2, \
                                   text = row, relief = tkinter.RIDGE, font='arial 10 bold italic', anchor='w').grid(row = c+1, column = 1,pady=3,padx=5)
             
                 en=tkinter.Text(root, width = 20, height = 1.5,\
                                    relief = tkinter.RIDGE,font='arial 9 ',undo=True)
                 en.grid(row = c+1, column = 2,pady=3,padx=1)
                 entries.append(en)
             c += 1
          r += 1
    tkinter.Button(root, text='Cancel',font='arial 10 bold italic', cursor="hand1",height=2,width=6, command=cancel).place(relx = 0.8, rely = 0.98, anchor = tkinter.SE)
    tkinter.Button(root, text='Save',font='arial 10 bold italic',cursor="hand1",height=2,width=5, command=save).place(relx = 0.979, rely = 0.98, anchor = tkinter.SE)
   