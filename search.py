#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:46:37 2020

@author: jenar
"""

import tkinter
from tkinter import messagebox
import csv


def search_id(file,id):
    row_no=0
    with open(file, "r",newline = "") as f:
        reader = csv.reader(f)
        for line_num, content in enumerate(reader):
            if content[0] == id:
                row_no=line_num
    
        
    title=''
    if row_no==0:
        title='Enter a valid team id'
    else:
        title='Team: '+str(id)
    root = tkinter.Toplevel()
    root.title(title)
    width = 450
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.configure(background="#B3B3B3")
    root.resizable(0,0)
    
    photo = tkinter.PhotoImage(file = "icon/task.gif")
    root.iconphoto(False, photo)
    
    
        
    # open file
    with open(file, newline = "") as file:
       reader = csv.reader(file)
    
       # r and c tell us where to grid the labels
       r = 0
       for col in reader:
          c = 0
          for row in col:
             # i've added some styling
             if (r==0):
                 tkinter.Label(root, width = 40, height = 2, \
                                   text = row, relief = tkinter.RIDGE, font='arial 10 bold italic', anchor='w').grid(row = c+1, column = 1,pady=3,padx=5)
             
             if (r==row_no):
                 tkinter.Label(root, width = 20, height = 2, \
                                   text = row, relief = tkinter.RIDGE, anchor='w').grid(row = c+1, column = 2,pady=3,padx=1)
             c += 1
          r += 1
          
    if row_no==0:
        messagebox.showerror("Error", "Enter a valid Team id...")
        root.destroy()
   