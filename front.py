import tkinter as tk
from tkinter import messagebox
from tkcalendar import dateentry
import sys
import os
from functools import partial
from tkinter import filedialog
import predict,show,editdb,addTeam
from search import *




#exit dialogbox
def ExitApplication():
  '''exit pop-up conformation box'''
  MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
  if MsgBox == 'yes':
    window.destroy()
    sys.exit(0)

#about
def info():
  '''for showing the pop-up information box'''
  messagebox.showinfo("Info", "A TechPie project successfully developed by Debabrata Tripathy,Sidhartha Bibekananda Dash,Subhashree Tripathy")

#to read the csv files
def read():
    #os.system("python read.py test.csv")
    show.show("test.csv")

def edit():
    def edit_team():
        id=en.get()
        if id=='':
            messagebox.showerror("Error", "Enter a Team id...")
            popup.destroy()
            popupmsg()
        popup.destroy()
        #os.system("python search.py test.csv %s" %(id))
        file="test.csv"
        editdb.edit_id(file,id)
    popup = tk.Toplevel()
    popup.wm_title("Enter Team-Id")
    width = 160
    height = 80
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
    popup.resizable(0,0)
    photo = tk.PhotoImage(file = "icon/task.gif")
    popup.iconphoto(False, photo)
    label = tk.Label(popup, text="Enter the team Id")
    label.pack()
    en=tk.Entry(popup,width=10)
    en.pack()
    tk.Button(popup, text="Search", command = edit_team).pack(pady=5)    
def add_team():
    addTeam.add_team("test.csv")
    
def popupmsg():
    def search_team():
        id=en.get()
        if id=='':
            messagebox.showerror("Error", "Enter a Team id...")
            popup.destroy()
            popupmsg()
        popup.destroy()
        #os.system("python search.py test.csv %s" %(id))
        file="test.csv"
        search_id(file,id)
    popup = tk.Toplevel()
    popup.wm_title("Search Team")
    width = 160
    height = 80
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
    popup.resizable(0,0)
    photo = tk.PhotoImage(file = "icon/task.gif")
    popup.iconphoto(False, photo)
    label = tk.Label(popup, text="Enter the team Id")
    label.pack()
    en=tk.Entry(popup,width=10)
    en.pack()
    tk.Button(popup, text="Search", command = search_team).pack(pady=5)
   
def reset():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    w1.set(5)
    ent.delete(0, 'end')
    
def warning(warn):
     messagebox.showwarning("Warning", "Enter %s..." %(warn))
     
     
def result(ar):
    popup = tk.Toplevel()
    popup.wm_title("Teams for the project")
    width = 210
    height = 150
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
    popup.resizable(0,0)
    photo = tk.PhotoImage(file = "icon/task.gif")
    popup.iconphoto(False, photo)

    
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
        
    Table_Frame=tk.Frame(popup,bd=2,relief=tk.RIDGE)
    Table_Frame.place(x=0,y=40,width=width,height=height-90)

    canvas = tk.Canvas(Table_Frame)
    canvas.place(width = width,height = height-90)
    scrollbar = tk.Scrollbar(Table_Frame, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', on_configure)
    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    tk.Label(popup,text="The eligible teams for this\nspecific projects is/are:",font = "Helvetica 10 bold ").pack(pady=10)
    
    for i in ar:
        def details(i,e):
            search_id("test.csv",str(i))
        l1=tk.Label(frame,text="Team no: "+str(int(i)),fg="blue",cursor="hand1")
        l1.bind("<Button-1>", partial(details,i))
        l1.pack()
        
    def save():
        folder_selected = filedialog.askdirectory()
        #print(folder_selected)
        if len(folder_selected)==0:
            return
        file_name = os.path.join(folder_selected,p_name+".txt")
        
        f = open(file_name,'w+')
        data = "Project name: "+p_name+"\nProject Duration: "+p_duration+"days\nStarting Date: "+p_date+"\nThe Eligible teams are:"
        count=0
        for i in ar:
            if count!=0:
                data=data+","
            data = data+" team"+str(int(i))
            count+=1
        f.write(data)
        f.close()
    tk.Button(popup, text="OK", command = popup.destroy).place(relx=0.75,rely=0.8)
    tk.Button(popup, text="Save", command = save).place(relx=0.4,rely=0.8)
    



def show_values():
    global priority
    global p_name
    global p_duration
    global p_date
    priority=w1.get()
    p_name=e1.get()
    p_duration=e2.get()
    p_date=ent.get()
    
    if p_name=='':
        warning("Project Name")
        return
    if p_duration=='':
        warning("Duration")
        return
    if p_date=='':
        warning("Date")
        return
    
    pq=-1
    if int(priority)<=3:
        pq=1
    elif int(priority)>3 and int(priority)<=7:
        pq=2
    elif int(priority)>7 and int(priority)<=10:
        pq=3
        
    result(predict.q[predict.q.Team_rating==pq].get("Team_name"))
    #print (e1.get(),e2.get(),priority,ent.get())
    #os.system("python predict.py %s %s %s %s" %(priority,p_name,p_duration,p_date))
    
    
window = tk.Tk()

window.title("Task manager")
width = 400
height = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.configure(background="#B3B3B3")
window.protocol("WM_DELETE_WINDOW",ExitApplication)
window.resizable(False,False)
#icon
if ( sys.platform.startswith('win')): 
    window.iconbitmap('icon/task.ico')
else:
    logo = tk.PhotoImage(file='icon/task.gif')
    window.call('wm', 'iconphoto', window._w, logo)
#menu bar
menubar = tk.Menu(window)

file = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Menu', menu = file) 
file.add_command(label ='Show team DB', command = read) 
file.add_command(label ='Edit team DB', command = edit) 
file.add_command(label ='Add team', command = add_team) 
file.add_separator() 
file.add_command(label ='Exit', command = ExitApplication) 

search = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Search', menu = search) 
search.add_command(label ='Search Team', command = popupmsg)

help_ = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='About', menu = help_) 
help_.add_command(label ='About', command = info)

window.config(menu = menubar) 
#end of menu bar


tk.Label(window,text="Task manager",font = "Helvetica 30 bold underline",fg='#000000',bg='#B3B3B3').place(relx=0.5,anchor=tk.N)


tk.Label(window, 
         text="Project Name",font='arial 10 bold italic').grid(row=2,padx=20, pady=(60,10), sticky=tk.W)
tk.Label(window, 
         text="Duration in days",font='arial 10 bold italic').grid(row=3,padx=20,pady=10, sticky=tk.W)
tk.Label(window, 
         text="Priority",font='arial 10 bold italic').grid(row=4,padx=20,pady=10, sticky=tk.W)
tk.Label(window, 
         text="Starting Date",font='arial 10 bold italic').grid(row=5,padx=20,pady=10, sticky=tk.W)

e1 = tk.Entry(window,width=28)
e2 = tk.Entry(window,width=28)

e1.grid(row=2, column=1,pady=(60,10), sticky=tk.W)
e2.grid(row=3, column=1,pady=5, sticky=tk.W)

w1 = tk.Scale(window, from_=1, to=10,length=200,orient=tk.HORIZONTAL)
w1.set(5)
w1.grid(row=4, column=1,pady=8, sticky=tk.W)

ent= dateentry.DateEntry( window, width=27,background="black", foreground="white",borderwidth=3)
ent.grid(row=5, column=1,pady=5, sticky=tk.W)

tk.Button(window, text='Reset',font='arial 10 bold italic', cursor="hand1", command=reset).grid(row=6, padx=20,column=0, sticky=tk.W, pady=10)
tk.Button(window, text='Show Eligible Teams',font='arial 10 bold italic',cursor="hand1", command=show_values).grid(row=6, column=1, sticky=tk.W, pady=10)

l4=tk.Label(window,text="A TechPie project",fg='#000000',bg='#B3B3B3',cursor="hand1")
l4.bind("<Button-1>", lambda e :info())
l4.place(relx=0.69,rely=0.95)

window.mainloop()