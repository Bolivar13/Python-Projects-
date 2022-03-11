import sqlite3
from tkinter import *
from tkinter import Label, filedialog, messagebox

con = sqlite3.connect('Database.db')
cur = con.cursor()

class Ajoutercontact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('550x600+600+200')
        self.title('Ajouter une contact ')
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='black')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='red')
        self.bottom.pack(fill=X)
        # fweewwe
        self.top_image = PhotoImage(file='icons/22.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='red')
        self.top_image_label.place(x=30, y=10)

        self.heading = Label(self.top, text='Ajouter une  contact', font='arial 15 bold', bg='red',
                             fg='black')
        self.heading.place(x=250, y=50)

        # Nom
        self.label_nom = Label(self.bottom, text=' Nom Complete :', font='Times 15 bold', fg='gold' , bg='black')
        self.label_nom.place(x=40, y=40)

        self.entry_nom = Entry(self.bottom, width=40, bd=4)
        self.entry_nom.place(x=190, y=40, height=30)
        # email
        self.label_email = Label(self.bottom, text=' Email                :', font='Times 16 bold', fg='gold', bg='black')
        self.label_email.place(x=40, y=80)

        self.entry_email = Entry(self.bottom, width=40, bd=4)
        self.entry_email.place(x=190, y=80, height=30)

        # phone number
        self.label_phone = Label(self.bottom, text=' N Telephone    :', font='Times 16 bold', fg='gold', bg='black')
        self.label_phone.place(x=40, y=120)

        self.entry_phone = Entry(self.bottom, width=40, bd=4)
        self.entry_phone.place(x=190, y=120, height=30)
        # Image
        self.label_image = Label(self.bottom, text=' image                :', font='Times 15 bold', fg='gold', bg='black')
        self.label_image.place(x=40, y=160)
        self.bimage = Button(self.bottom, text=' Parcourir ', font='Times', fg='black', bg='gold',command=self.Parcourirphoto)
        self.bimage.place(x=444, y=160, height=30)
        self.entry_image = Entry(self.bottom, width=40, bd=4)
        self.entry_image.place(x=190, y=160, height=30)

        # button
        button = Button(self.bottom, text='Ajouter ', font='Times 14 bold', fg='red', bg='black', command=self.add_people)
        button.place(x=250, y=330)
    #sélectionner une photo
    def Parcourirphoto(self):
        self.entry_image.delete(0,END)
        self.filename = filedialog.askopenfilename(initialdir ="/",title ="Choisir une image")
        self.entry_image.insert(END,self.filename)
    #enregistrer l'image en binaire dans Data base
    def convertToBinaryData(self,evet):
        with open(evet, 'rb') as file:
            blobData = file.read()
        return blobData
    def add_people(self):
        name = self.entry_nom.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        filename = self.entry_image.get()
        Profile = self.convertToBinaryData(filename)
        if not name or not email or phone == '':
            messagebox.showerror('Error', 'fill all the fields', icon='warning')
        else:
            try:
                query = 'insert into "Contacts"(Nom_complete, N_telephone, email,image) values (?,?,?,?)'
                cur.execute(query, (name, email, phone,Profile))
                #enregistre L'image dans le dossier images/
                def writeTofile(data, filename):
                    with open(filename, 'wb') as file:
                        file.write(data)
                photoPath = "images/profile_"+str(name) +"."+ "jpg"
                writeTofile(Profile,photoPath)
                #########################################
                con.commit()
                messagebox.showerror('success', 'le contact est ajoute',icon='info')
                self.destroy()
            except EXCEPTION as e:
                messagebox.showerror('Error', str(e), icon='error')
