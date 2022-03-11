from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

from Ajouter_contacts import Ajoutercontact
from infos_contacts import Infor
from Modifier_contacts import Modifier

con = sqlite3.connect('database.db')
cur = con.cursor()

class MesContacts(Toplevel):
    def __init__(self) -> object:

        Toplevel.__init__(self)
        self.geometry('650x650+600+200')
        self.title('Mes Contacts')
        self.resizable(False, False)

        self.top = Frame(self, height=155, bg='red')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=450, bg='black')
        self.bottom.pack(fill=X)
        
        self.heading = Label(self.top, text='Mes Contacts', font='arial 15 bold', bg='red', fg='black')
        self.heading.place(x=230, y=50)


        self.top_image = PhotoImage(file='icons/22.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='red')
        self.top_image_label.place(x=30, y=10)





        # Search area
        self.lbSearchByName = PhotoImage(file='icons/rech1.png')
        self.lbSearchByName_label = Label(self,image=self.lbSearchByName, bg='white')
        self.lbSearchByName_label.place(x=173, y=124)
        self.entrySearchByName = Entry(self, font=("Times", 11), bd=4)
        self.entrySearchByName.bind("<Return>" , self.searchByNom)
        self.entrySearchByName.place(x=3, y=128, width=170, height=26)
       
       
        # Buttons
        self.add_label = Label(self.bottom,text=' Ajouter Contact      ', font='Times 15 bold', bg='black', fg='red')
        self.add_label.place(x=450, y=22)
        self.bottom_ajou = PhotoImage(file='icons/ajout.png')
        btnadd = Button(self.bottom,image=self.bottom_ajou, bg='black',
        command=self.Ajouter_contact)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)
        btnadd.place(x=400,y=15)

        self.mod_label = Label(self.bottom,text=' Modifier contact      ', font='Times 15 bold', bg='black', fg='red')
        self.mod_label.place(x=450, y=77)
        self.bottom_mod = PhotoImage(file='icons/modif.png')
        btnUpdate = Button(self.bottom,image=self.bottom_mod, bg='black',
                           command=self.Modifier_function)
        btnUpdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)
        btnUpdate.place(x=400,y=70)


        self.inf_label = Label(self.bottom,text=' les infos du contact', font='Times 15 bold', bg='black', fg='red')
        self.inf_label.place(x=450, y=132)
        self.bottom_inf = PhotoImage(file='icons/info2.png')
        btnDisplay = Button(self.bottom,image=self.bottom_inf, bg='black',
                             command=self.infor_personne)
        btnDisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)
        btnDisplay.place(x=400,y=125)

        self.supp_label = Label(self.bottom,text=' Supprimer le contact', font='Times 14 bold', bg='black', fg='red')
        self.supp_label.place(x=450, y=187)
        self.bottom_sup = PhotoImage(file='icons/delt.png')
        btnsuppri = Button(self.bottom,image=self.bottom_sup, bg='black',
                           command=self.supprimer_personne)
        btnsuppri.grid(row=0, column=2, padx=20, pady=130, sticky=N)
        btnsuppri.place(x=400,y=180)

        # Ajouter une arborescence
        self.liste = ttk.Treeview(self.bottom, columns =(1,2,3,4,5), height = 5, show ="headings")
        self.liste.place(x=20, y=1, width = 370, height =400)
       
        #  titres
        self.liste.heading(1, text ="N°")
        self.liste.heading(2, text = "Nom et Prenom ")
        self.liste.heading(3, text = "Email")
        self.liste.heading(4, text = " N° Telephone")
         
        self.liste.column(1, width=40)
        self.liste.column(2, width=100)
        self.liste.column(3, width=90)
        
         
        # Afficher les données dans l'objet treeview

        
        conn = sqlite3.connect('Database.db')
        cur = conn.cursor()
        select = cur.execute("select*from Contacts")
        for row in select:
            self.liste.insert('' , END , values = row)
    def searchByNom(self,evet):
        
        for x in self.liste.get_children():
            self.liste.delete(x)
        nom = self.entrySearchByName.get()
        conn = sqlite3.connect("Database.db")
        cur =conn.cursor()
        select = cur.execute("SELECT*FROM contacts where Nom_complete = (?)",(nom,))
        conn.commit()
        for row in select:
            self.liste.insert('' , END , values = row)
        conn.close()
    def Ajouter_contact(self):
        Ajoutercontact()
        self.destroy()
    def supprimer_personne(self):
        try:
            NSlect = self.liste.item(self.liste.selection())['values'][0]
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            Supprimer = 'delete from contacts where id = {} '.format(NSlect)
            string_for_mbox = 'voulez-vous vraiment supprimer?'
            answer = messagebox.askquestion('Warning', string_for_mbox)
            if answer == 'yes':
                try:
                    cur.execute(Supprimer)
                    conn.commit()
                    messagebox.showinfo('Success', 'Deleted')
                    self.destroy()
                except Exception as e:
                    messagebox.showinfo('Info', str(e))
        except IndexError:
            messagebox.showinfo('Error', "Voulez-vous sélectionner votre choix", icon='error')


    def Modifier_function(self):
        try:
            NSlect = self.liste.item(self.liste.selection())['values'][0]
            Modifier(NSlect)
        except IndexError:
            messagebox.showinfo('Error', "Voulez-vous sélectionner votre choix", icon='error')
    def infor_personne(self):
        try:
            NSlect = self.liste.item(self.liste.selection())['values'][0]
            Infor(NSlect)
        except IndexError:
            messagebox.showinfo('Error', "Voulez-vous sélectionner votre choix", icon='error')
