from tkinter import *
import sqlite3
from PIL import Image,ImageTk

con = sqlite3.connect('Database.db')
cur = con.cursor()

class Infor(Toplevel):
    def __init__(self, id):
        Toplevel.__init__(self)

        self.geometry('650x650+600+200')
        self.title('les informations du contact')
        self.resizable(False,False)

        query = 'select * from Contacts where id = "{}"'.format(id)
        result = cur.execute(query).fetchone()
        self.person_id = id
        Nom_complete = result[1]
        N_telephone = result[2]
        email = result[3]

        self.top = Frame(self, height=150, bg='black')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='red')
        self.bottom.pack(fill=X)
        # fweewwe
        self.top_image = PhotoImage(file='icons/modi3.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='black')
        self.top_image_label.place(x=30, y=10)

        self.heading = Label(self.top, text='les informations du contact',  font='arial 15 bold', bg='red',
                             fg='black')
        self.heading.place(x=230, y=50)


        # Nom
        self.label_nom = Label(self.bottom, text=' Nom Complete :', font='Times 15 bold', fg='black', bg='gold')
        self.label_nom.place(x=40, y=40)

        self.entry_nom = Entry(self.bottom, width=40, bd=4)
        self.entry_nom.place(x=190, y=40, height=30)
        self.entry_nom.insert(0, Nom_complete)
        self.entry_nom.config(stat='disabled')
        # email
        self.label_email = Label(self.bottom, text=' Email                :', font='Times 16 bold', fg='black', bg='gold')
        self.label_email.place(x=40, y=80)

        self.entry_email = Entry(self.bottom, width=40, bd=4)
        self.entry_email.place(x=190, y=80, height=30)
        self.entry_email.insert(0, email)
        self.entry_email.config(stat='disabled')

        # phone number
        self.label_phone = Label(self.bottom, text=' N Telephone    :', font='Times 16 bold', fg='black', bg='gold')
        self.label_phone.place(x=40, y=120)
        self.entry_phone = Entry(self.bottom, width=40, bd=4)
        self.entry_phone.place(x=190, y=120, height=30)
        self.entry_phone.insert(0, N_telephone)
        self.entry_phone.config(stat='disabled')
        #Image
        try:
            mgProfile = "images/profile_"+ str(Nom_complete) + "." + "jpg"
            self.load = Image.open(mgProfile)
            self.load.thumbnail((130, 130))
            self.photo = ImageTk.PhotoImage(self.load)
            self.label_image = Label(self.bottom, image=self.photo)
            self.label_image.place(x=480, y=30)
        except:
            self.load = Image.open("images/profile.png")
            self.load.thumbnail((130, 130))
            self.photo = ImageTk.PhotoImage(self.load)
            self.label_image = Label(self.bottom, image=self.photo)
            self.label_image.place(x=480, y=30)

