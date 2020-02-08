from tkinter import *
import os



def Get_info():
 global screen4
 screen4 = Tk()
 screen4.title("Get info")
 screen4.geometry("350x300")

 global name
 global name_Entry

 name = StringVar()

 Label(screen4, text = "Get info", font = ("Arial black", 20), height = "2", width = "20").pack()
 Label(screen4, text = "Give name : ", font = ("Arial black", 10)).pack()
 name_Entry = Entry(screen4, textvariable = name)
 name_Entry.pack()
 Label(screen4,text = "").pack()
 Button(screen4,text = "Get", width = "20", height = "2", command = info).pack()
 screen4.mainloop()

def info():
    name_info = name.get()
    name_Entry.delete(0, END)
    check_list = os.listdir()

    name_info += ".txt"
    if name_info in check_list :
      with open(name_info,"r") as fic:
          vir = fic.read().splitlines()
          
      Label(screen4,text = vir[0]).pack()
      Label(screen4,text = vir[1]).pack()
      Label(screen4,text = vir[2]).pack()
    else:
        Label(screen4, text = "Client not found", fg ="red").pack()

def Check_out():
    print("")


def Check_in():

 Firstname_info = Firstname.get()
 Familyname_info = Familyname.get()
 Number_info = Number.get()
 Number_of_days_info = Number_of_days.get()
 RoomNumber_info=RoomNumber.get()
 print(Familyname_info)

 with open(Familyname_info +".txt","w") as file:
     file.write(Firstname_info+"\n")
     file.write(Familyname_info+"\n")
     file.write(Number_info+"\n")
     file.write(Number_of_days_info+"\n")
     file.write(RoomNumber_info)

 Firstname_Entry.delete(0, END)
 Familyname_Entry.delete(0, END)
 Number_Entry.delete(0, END)
 Number_of_days_Entry.delete(0, END)
 RoomNumber_Entry.delete(0,END)

 Label(screen2, text="Registration succes", fg = "green").pack()


def Checkin_screen():
 global screen2
 screen2 = Tk()
 screen2.title("Check in")
 screen2.geometry("300x400")
 global Firstname_Entry
 global Familyname_Entry
 global Number_Entry
 global Number_of_days_Entry
 global RoomNumber_Entry 


 global Firstname
 global Familyname
 global Number
 global Number_of_days
 global RoomNumber


 Firstname = StringVar()
 Familyname = StringVar()
 Number = StringVar()
 Number_of_days = StringVar()
 RoomNumber=StringVar()

 Label(screen2, text = "Welcome", font = ("Arial black", 20), height = "2").pack()

 Label(screen2, text = "Firstname", font = ("Arial black", 10)).pack()
 Firstname_Entry = Entry(screen2 , textvariable = Firstname)
 Firstname_Entry.pack()

 Label(screen2, text = "Familyname", font = ("Arial black", 10)).pack()
 Familyname_Entry = Entry(screen2 , textvariable = Familyname)
 Familyname_Entry.pack()

 Label(screen2, text = "Number", font = ("Arial black", 10)).pack()
 Number_Entry = Entry(screen2 , textvariable = Number)
 Number_Entry.pack()

 Label(screen2,text="RoomNumber",font= ("Arial black", 10)).pack()
 RoomNumber_Entry=Entry(screen2,textvariable=RoomNumber)
 RoomNumber_Entry.pack()

 Label(screen2,text="Number_of_days",font= ("Arial black", 10)).pack()
 Number_of_days_Entry=Entry(screen2,textvariable= Number_of_days)
 Number_of_days_Entry.pack()

 Label(screen2, text ="").pack()
 Button(screen2,text = "Submit", height = "2", width = "20", command = Check_in).pack()

 screen2.mainloop()




def Check_out_screen():
 global screen3
 screen3 = Tk()
 screen3.geometry("300x280")
 screen3.title("Check out")
 global room
 global room_Entry
 room = StringVar()
 Label(screen3, text = "Check out ", font = ("Arial black", 25), height = "2", width = "20").pack()
 Label(screen3, text = "Room number :", font = ("Arial black", 10)).pack()
 room_Entry = Entry(screen3, textvariable = room)
 room_Entry.pack()
 Label(screen3, text = "").pack()
 Button(screen3, text = "Ok", command = Check_out, height = "2", width = "20").pack()
 screen3.mainloop()

def Welcome_screen():
 global screen1
 screen1= Tk()
 screen1.geometry("380x480")
 screen1.title("Welcome Page")
 screen1.maxsize(380, 480)
 screen1.minsize(380, 480)
 Label(screen1,text = "Welcome", height= "2", width = "30", font = ("Arial black", 25)).pack()
 Button(screen1, text =  "Check in", width = "30", height = "2", font = ("Arial black", 10), command = Checkin_screen).pack()
 Label(screen1,text = "").pack()
 Button(screen1, text =  "Check out", width = "30", height = "2", font = ("Arial black", 10), command = Check_out_screen).pack()
 Label(screen1,text = "").pack()
 Button(screen1, text =  "Get info", width = "30", height = "2", font = ("Arial black", 10), command = Get_info).pack()
 Label(screen1,text = "").pack()
 Button(screen1, text =  "Exit", width = "30", height = "2", font = ("Arial black", 10)).pack()
 screen1.mainloop()



def login_virify():
    username=username_virify.get()
    password=password_virify.get()


    username_entry.delete(0,END)
    password_entry.delete(0,END)


    list=os.listdir()
   
    username+=".txt"
 
    if username in list :
        with open(username,"r") as file:
            virify = file.read().splitlines()
            if password in virify :
                Welcome_screen()
            else:
                Label(screen,text="password Error",fg="red").pack()

    else :
        Label(screen,text="Error",fg="red").pack()




def login_screen ():
 global screen
 screen= Tk()
 #screen.minsize=(400,250)
 #screen.maxsize=(300,250)
 screen.title("Login")
 screen.geometry("300x250")
 global username_virify
 global password_virify

 global username_entry
 global password_entry

 username_virify=StringVar()
 password_virify=StringVar()

 Label(screen, text="login", font=("Arial black",25)).pack()
 Label(screen, text="").pack()
 Label(screen,text="username",font=("Arial black",10)).pack()
 username_entry=Entry(screen, textvariable=username_virify)
 username_entry.pack()
 Label(screen, text="password",font=("Arial black",10)).pack()
 password_entry=Entry(screen, textvariable=password_virify, show="*")
 password_entry.pack()
 Label(screen, text="").pack()
 Button(screen, text="login", height="2", width="20",command=login_virify).pack()
 Label(screen, text="").pack()
 screen.mainloop()


login_screen()