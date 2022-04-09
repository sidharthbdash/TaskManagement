import tkinter
import csv
import sys




def show(file): 
        
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
        
    root = tkinter.Toplevel()
    root.title("DataBase")
    #root.resizable(False,False)
    
    screen_width = root.winfo_screenwidth()-20
    screen_height = root.winfo_screenheight()-50
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()-35
    root.geometry("%dx%d+0+0" % (w, h))
    root.resizable(0,0)
    if ( sys.platform.startswith('win')): 
        root.iconbitmap('icon/task.ico')
    else:
        photo = tkinter.PhotoImage(file = "icon/task.gif")
        root.iconphoto(False, photo)
    
    
    canvas = tkinter.Canvas(root)
    canvas.place(width = screen_width,height = screen_height)
    scrollbar = tkinter.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    canvas.configure(yscrollcommand = scrollbar.set)
    
    scrollbarV = tkinter.Scrollbar(root, command=canvas.xview,orient=tkinter.HORIZONTAL)
    scrollbarV.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.configure(xscrollcommand = scrollbarV.set)
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', on_configure)
    
    # --- put frame in canvas ---
    
    frame = tkinter.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    
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
                 label = tkinter.Label(frame, width = 30, height = 2, \
                                   text = row, relief = tkinter.RIDGE, font='arial 10 bold italic')
             else:
                 label = tkinter.Label(frame, width = 30, height = 2, \
                                   text = row, relief = tkinter.RIDGE)
             label.grid(row = r, column = c)
             c += 1
          r += 1

