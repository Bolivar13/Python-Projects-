from tkinter import *
import sqlite3
from tkinter import messagebox

from PIL import Image,ImageTk

con = sqlite3.connect('database.db')
cur = con.cursor()

class Modifier(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry('620x600+600+200')
        self.title('Modifier le contact ')
        self.resizable(False,False)

        query = 'select * from Contacts where id = "{}"'.format(person_id)
        result = cur.execute(query).fetchone()
        self.person_id = person_id
        person_name = result[1]
        person_email = result[3]
        person_phone = result[2]
         

        self.top = Frame(self, height=150, bg='black')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='black')
        self.bottom.pack(fill=X)
        #
        self.top_image = PhotoImage(file='icons/m.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=30, y=10)
        self.heading = Label(self.top, text='Modifier le contact' ,font='arial 15 bold', bg='red',
                             fg='black')
        self.heading.place(x=230, y=50)
                # NOM
        self.label_nom = Label(self.bottom, text=' Nom Complete :', font='Times 15 bold', fg='black', bg='gold')
        self.label_nom.place(x=40, y=40)
        self.entry_nom = Entry(self.bottom, width=40, bd=4)
        self.entry_nom.place(x=190, y=40, height=30)
        self.entry_nom.insert(0, person_name)
        # email
        self.label_email = Label(self.bottom, text=' N Telephone                :', font='Times 16 bold', fg='black', bg='gold')
        self.label_email.place(x=40, y=80)

        self.entry_email = Entry(self.bottom, width=40, bd=4)
        self.entry_email.place(x=190, y=80, height=30)
        self.entry_email.insert(0, person_email)
        # phone number
        self.label_phone = Label(self.bottom, text=' Email                 :', font='Times 16 bold', fg='black', bg='gold')
        self.label_phone.place(x=40, y=120)

        self.entry_phone = Entry(self.bottom, width=40, bd=4)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=190, y=120, height=30)
        #Image
        try:
            mgProfile = "images/profile_"+ str(person_name) + "." + "jpg"
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
        # button
        button = Button(self.bottom, text='Enregister', font='Times 14 bold', fg='black', bg='red', command=self.update_people)
        button.place(x=260, y=330)

    def update_people(self):
        id = self.person_id
        name = self.entry_nom.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        if not name or not email or phone == '':
            messagebox.showerror('Error', 'fill all the fields', icon='warning')
        #déclarer la modification
        query = 'update Contacts set Nom_complete = "{}", N_telephone = "{}", email = "{}" where id = {}'.format(name, phone, email, id)
        try:
            #appliquer la modification
            cur.execute(query)
            con.commit()
            messagebox.showinfo('success', 'contact est modifier  ', icon='info')
            self.destroy()
        except Exception as e:
            messagebox.showinfo('Warning', str(e), icon='Warning !!')
