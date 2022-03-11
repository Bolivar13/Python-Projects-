from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3


def Database():
    global conn, cursor
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")

def DisplayForm():
    
    display_screen = Tk()
    display_screen.geometry("990x450")
    display_screen.title("CONTACTS ")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
     
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

 


    #first header

    LFrom = Frame(display_screen, width="350" , height="10",bg="black")
    LFrom.pack(side=LEFT, fill=Y)

    #second header

    LeftViewForm = Frame(display_screen, width=500,bg="red")
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    
    lbl_text = Label(TopViewForm, text="📵 Contact Manager 📵 ", font=('verdana', 18), width=600, height=3 , bg="red")
    lbl_text.pack(fill=X)
    
    Label(LFrom, text="Nom  ", font=("Arial", 12),bg="black",fg="red").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Prenom ", font=("Arial", 12),bg="black",fg="red").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Sexe ", font=("Arial", 12),bg="black",fg="red").pack(side=TOP)

    gender.set("Sélectionnez le sexe " )
    content={'Male','Female'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Addresse ", font=("Arial", 12),bg="black",fg="red").pack(side=TOP)
    Entry(LFrom, font=("Helvetica", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="N Telephone ", font=("Arial", 12),bg="black",fg="red").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Enrigestrer",font=("Arial", 10, "bold") , command=Enrigestrer , bg="black",fg="red").pack(side=TOP, padx=10,pady=5, fill=X)

    
    lbl_txtsearch = Label(LeftViewForm, text="Entrez Le Nom pour rechercher", font=('verdana', 10),bg="red")
    lbl_txtsearch.pack()
    
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    
    btn_search = Button(LeftViewForm, text="Chercher", command=SearchRecord,bg="black" , fg="red")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_view = Button(LeftViewForm, text="Voir tout", command=DisplayData,bg="black" , fg="red")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_Reinitialiser = Button(LeftViewForm, text=" réinitialiser ", command=Reinitialiser,bg="black"  , fg="red")
    btn_Reinitialiser.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftViewForm, text="Supprimer", command=Delete,bg="black"  , fg="red")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    
    btn_delete = Button(LeftViewForm, text="Modifier", command=Update,bg="black"  , fg="red")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    

    btn_quit = Button(LeftViewForm, text="Quitter", command=quit,bg="gold"  , fg="black" , width="4" , height="5" , border="8" , )
    btn_quit.pack(side=TOP, padx=10, pady=10, fill=X)


    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm ,columns=("Person ID", "Name", "Prenom", "Sexe","Adresse","Telephone"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    tree.heading('Person ID', text="ID",  )
    tree.heading('Name', text="Nom",  )
    tree.heading('Prenom', text="Prenom",  )
    tree.heading('Sexe', text="Sexe",  )
    tree.heading('Adresse', text="Addresse",  )
    tree.heading('Telephone', text="Telephone",  )
     
     
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def Update():
    Database()
     
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
     
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","Sélectionnez un  Contact Pour Modifier !!!")
    else:
         
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        
        conn.execute('Update REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?',(fname1,lname1,gender1,address1,contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message"," le contact est modifié !!")
        
        Reinitialiser()
         
        DisplayData()
        conn.close()

def Enrigestrer():
    Database()
    
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
       
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)',(fname1,lname1,gender1,address1,contact1));
        conn.commit()
        tkMessageBox.showinfo("Message","le contact est ajouté !!")
        
        DisplayData()
        conn.close()
def Reinitialiser():
     
    tree.delete(*tree.get_children())
     
    DisplayData()
     
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")

def Delete():
     
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Attention !! ","Sélectionnez un contact pour Supprimer !!")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Voulez-vous vraiment supprimer ce contact !?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute(" SUPP FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def SearchRecord():

    Database()
  
    if SEARCH.get() != "":
      
        tree.delete(*tree.get_children())
       
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE FNAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
       
        fetch = cursor.fetchall()
      
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def DisplayData():
    
    Database()
   
    tree.delete(*tree.get_children())
    
    cursor=conn.execute("SELECT * FROM REGISTRATION")
    
    fetch = cursor.fetchall()
    
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
   
    fname.set(selecteditem[1])
    lname.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])

DisplayForm()
if __name__=='__main__':
    mainloop()