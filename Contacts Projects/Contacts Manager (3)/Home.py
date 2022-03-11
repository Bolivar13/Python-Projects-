from tkinter import *
from Mes_Contacts import MesContacts
from Ajouter_contacts import Ajoutercontact

class Application (object):
    def __init__(self,master):
        self.master = master
        self.top = Frame(master, height=168,bg='Red')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500,bg='black')
        self.bottom.pack(fill=X)
        #fweewwe
        self.top_image = PhotoImage(file='icons/contacts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='red' )
        self.top_image_label.place(x=90, y=10)

 

        self.heading = Label(self.top, text='Contacts Manager',font='Times 20 bold' , bg='red' , fg='Black')
        self.heading.place(x=270, y=50)

   

        self.viewButton = Button(self.bottom, text='  Contacts Manager  ', font='Times 14 bold',command=self.mes_contacts, fg='black', bg='red')
        self.viewButton.place(x=250, y=140)
        

        self.addButton = Button(self.bottom, text='Quitter ', font='Times 14 bold', fg='red', bg='black',command=quit)
        self.addButton.place(x=300, y=200)

        


    def mes_contacts(self):
        MesContacts()
    def Ajouter_Contacts(self):
        Ajoutercontact()


def main():
    root=Tk()
    app =Application(root)
    root.title('Contacts')
    root.geometry('650x600+350+200')
    root.resizable(False,False)
    root.mainloop()
if __name__ == '__main__':
    main()