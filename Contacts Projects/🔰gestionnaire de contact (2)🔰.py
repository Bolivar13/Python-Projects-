from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
from tkinter.messagebox import *
from tkinter import filedialog


app = Tk()
app.geometry("600x420")
app.title('  Contact Manager')
app.resizable(False, False) 
photo = PhotoImage(file = "contacts.png")
app.iconphoto(False, photo)


bloc_original = Canvas(app, width=650, height=540, bg='red')
bloc_original.place(x=10,y=10)
bg = PhotoImage(file='25.png')
bloc_original.create_image(350, 200, image=bg)



def ajouter():
    ajout_gui=Toplevel(app)
    ajout_gui.geometry("300x300")
    ajout_gui.title("Information du contact")
    photo = PhotoImage(file = "icons/ajout.png")
    ajout_gui.iconphoto(False, photo)
    ajout_gui['bg'] = 'dark slate gray'




    def confirmer():
        test = "done!"
        nom = name.get(1.0, END+"-1c")
        last_nam = last_name.get(1.0, END+"-1c")
        num = Num.get(1.0, END+"-1c")
        adr = Adr.get(1.0, END+"-1c")
        liste = [nom,last_nam,num,adr]
        for s in liste:
            if s=="":
                test = "retry"
                Message.configure(text="Completez les données!")
        if test != "retry":
            try:
                file = open('contact.txt','a')
                file.write(nom+'  '+last_nam+'          '+num+'          '+adr+'          '+filename)
                file.write('\n')
                file.close()
                ajout_gui.destroy()
            except:
                Message.configure(text="Completez les données!")          


    ######
    def charger():
        global filename
        filename = filedialog.askopenfilename()
        state_picture = 'Done'
        Img_label_2.configure(text=filename)
        return filename
        
    name_label=Label(ajout_gui, text="Nom",bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    name_label.place(x=20 ,y=20)
    name=Text(ajout_gui, height = 1, width = 20)
    name.place(x=85 ,y=20)

    last_name_label=Label(ajout_gui, text="Prenom",bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    last_name_label.place(x=20 ,y=50)
    last_name=Text(ajout_gui, height = 1, width = 20)
    last_name.place(x=85 ,y=50)

    Num_label=Label(ajout_gui, text="Numero",bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    Num_label.place(x=20 ,y=80)
    Num=Text(ajout_gui, height = 1, width = 20)
    Num.place(x=85 ,y=80)

    Adr_label=Label(ajout_gui, text="Adresse",bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    Adr_label.place(x=20 ,y=110)
    Adr=Text(ajout_gui, height = 1, width = 20)
    Adr.place(x=85 ,y=110)


     



    Img_label=Label(ajout_gui, text="Image",bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    Img_label.place(x=20 ,y=140)
    charger = ttk.Button(ajout_gui,text = "Parcourir",command = charger)
    charger.place(x=20 ,y=165)
    Img_label_2=Label(ajout_gui,bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    Img_label_2.place(x=85 ,y=140)

    Message=Label(ajout_gui,bg='dark slate gray',fg='black',font = "Verdana 10 bold")
    Message.place(x=90 ,y=210)
    
    Button_ajout_2 = ttk.Button(ajout_gui,text = "Enrigestrer",command = confirmer)
    Button_ajout_2.place(x=100 ,y=245)
    


def supprimer():
    supp_gui=Toplevel(app)
    supp_gui.geometry("600x100")
    supp_gui.title("Supprimer contact")
    photo_2 = PhotoImage(file = "icons/delt.png")
    supp_gui.iconphoto(False, photo_2)
    supp_gui['bg'] = 'dark slate gray'
    supp_gui.resizable(False, False)
    


    def delete():
        name = nom_supp.get(1.0, END+"-1c")
        found = 0
        if name=='':
            Message.configure(text="Donnez le nom du contact à supprimer!")

        else:
            nom_1 = name
            file = open('contact.txt','r')
            data = file.readlines()
            for l in data:
                d = l.split(' ')
                if d[0] == nom_1:
                    found = 1
                    data.remove(l)
                    
            file.close()
            file = open('contact.txt','w')
            for k in data:
                file.write(k)
            file.close()
            if found == 1:
                Message.configure(text="Done!")
            else:
                Message.configure(text="Not Found")


    def fermer():
        supp_gui.destroy()
    
    nom_label=Label(supp_gui, text="Nom",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    nom_label.place(x=20 ,y=20)
    nom_supp=Text(supp_gui, height = 1, width = 20)
    nom_supp.place(x=80 ,y=20)
    delete = ttk.Button(supp_gui,text = "Supprimer",command = delete)
    delete.place(x=300,y=5)
    ferm= ttk.Button(supp_gui,text = "Quitter",command = fermer)
    ferm.place(x=400,y=5)
    Message=Label(supp_gui,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    Message.place(x=150 ,y=60)
    

def modifier():
    mod_gui=Toplevel(app)
    mod_gui.geometry("620x500")
    mod_gui.title("Modifier contact")
    photo_3 = PhotoImage(file = "modify.png")
    mod_gui.iconphoto(False, photo_3)
    app.resizable(False, False) 

    bloc1 = Canvas(mod_gui, width=620, height=50, bg='dark slate gray')
    bloc2 = Canvas(mod_gui, width=620, height=450, bg='dark slate gray')
    bloc3 = Canvas(mod_gui, width=620, height=450, bg='dark slate gray')
    bloc1.place(x=0,y=0)
    bloc3.place(x=0,y=51)


    def charger_info():
        global new_filename
        global name
        name = nom_mod.get(1.0, END+"-1c")
        test_name = 0
        if name=='':
            Message_label.configure(text="Donnez le nom du contact à modifier!")
            bloc2.place_forget()
            bloc3.place(x=0,y=51)
        else:
            file = open('contact.txt','r')
            data = file.readlines()
            for l in data:
                d=l.split('        ')
                n=d[0].split('  ')
                m=n[0]+' '+n[1]
                if n[0]==name:
                    test_name = 1
                    anc_nom_label.configure(text='Ancien nom: '+n[0])
                    anc_prenom_label.configure(text='Ancien prenom: '+n[1])
                    anc_num_label.configure(text='Ancien numero: '+d[1])
                    anc_adr_label.configure(text='Ancienne adresse: '+d[2])
                    anc_pic_label.configure(text='Ancienne photo: '+d[3])
                    break
            file.close()
            if test_name == 1:
                new_filename=''
                bloc3.place_forget()
                bloc2.place(x=0,y=51)
            else:
                Message_label.configure(text="Contact Introuvable!")
                bloc2.place_forget()
                bloc3.place(x=0,y=51)
        

    def update_info():
        newnom = new_nom.get(1.0, END+"-1c")
        newprenom = new_prenom.get(1.0, END+"-1c")
        newnum = new_num.get(1.0, END+"-1c")
        newadr = new_adr.get(1.0, END+"-1c")

        nom_1 = name
        file = open('contact.txt','r')
        data = file.readlines()
        for l in data:
            d=l.split('        ')
            n=d[0].split('  ')
            m=n[0]+' '+n[1]
            if n[0]==nom_1:
                if newnom != '':
                    n[0]=newnom
                if newprenom != '':
                    n[1]=newprenom
                d[0] = n[0]+'  '+n[1]
                if newnum != '':
                    d[1] = '  '+newnum
                if newadr != '':
                    d[2] = '  '+newadr
                if new_filename != '':
                    d[3] = '  '+new_filename+'\n'
                    
                liste_new_data = d[0]+'        '+d[1]+'        '+d[2]+'        '+d[3]

                data[data.index(l)] = liste_new_data
                break
        file.close()
        file = open('contact.txt','w')
        for k in data:
            file.write(k)
        file.close()
        Message_label.configure(text="Done!")
        bloc2.place_forget()
        bloc3.place(x=0,y=51)
        
    def New_charge():
        global new_filename
        new_filename = filedialog.askopenfilename()
        new_pic_label_2.configure(text=new_filename)
        return new_filename
        
    def fermer():
        mod_gui.destroy()
    
    nom_label=Label(bloc1, text="Nom",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    nom_label.place(x=20 ,y=20)
    nom_mod=Text(bloc1, height = 1, width = 20)
    nom_mod.place(x=80 ,y=20)
    data_charge = ttk.Button(bloc1,text = "Charger",command = charger_info)
    data_charge.place(x=320,y=5)
    ferm= ttk.Button(bloc1,text = "Fermer",command = fermer)
    ferm.place(x=420,y=5)
    
    anc_nom_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    anc_nom_label.place(x=20 ,y=20)
    anc_prenom_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    anc_prenom_label.place(x=20 ,y=90)
    anc_num_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    anc_num_label.place(x=20 ,y=160)
    anc_adr_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    anc_adr_label.place(x=20 ,y=230)
    anc_pic_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    anc_pic_label.place(x=20 ,y=300)

    new_nom_label=Label(bloc2, text="Nouveau nom",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    new_nom_label.place(x=300 ,y=55)
    new_prenom_label=Label(bloc2, text="Nouveau prenom",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    new_prenom_label.place(x=300 ,y=125)
    new_num_label=Label(bloc2, text="Nouveau numero",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    new_num_label.place(x=300 ,y=195)
    new_adr_label=Label(bloc2, text="Nouvelle adresse",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    new_adr_label.place(x=300 ,y=265)
    new_pic_label=Label(bloc2, text="Nouvelle photo",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    new_pic_label.place(x=300 ,y=335)
    new_pic_label_2=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    new_pic_label_2.place(x=430 ,y=335)

    new_nom=Text(bloc2, height = 1, width = 20)
    new_nom.place(x=430 ,y=55)
    new_prenom=Text(bloc2, height = 1, width = 20)
    new_prenom.place(x=430 ,y=125)
    new_num=Text(bloc2, height = 1, width = 20)
    new_num.place(x=430 ,y=195)
    new_adr=Text(bloc2, height = 1, width = 20)
    new_adr.place(x=430 ,y=265)

    new_charge= ttk.Button(bloc2,text = "Charger photo",command = New_charge)
    new_charge.place(x=400,y=380)
    mod = ttk.Button(bloc2,text = "Modifier",command = update_info)
    mod.place(x=200,y=390)
    
    Message_label=Label(bloc3,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    Message_label.place(x=150 ,y=20)
    
def afficher():
    affich_gui=Toplevel(app)
    affich_gui.geometry("600x296")
    affich_gui.title("Liste de contactes")
    photo_4 = PhotoImage(file = "afficher.png")
    affich_gui.iconphoto(False, photo_4)
    affich_gui['bg'] = 'azure2'
    app.resizable(False, False) 

    def close():
        affich_gui.destroy()
    
    scrollbar = Scrollbar(affich_gui)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(affich_gui, yscrollcommand = scrollbar.set )
    file = open('contact.txt','r')
    data = file.readlines()
    for e in data:
        mylist.insert(END, e)
        mylist.insert(END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    mylist.pack( ipadx= 180, side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    fermer = Button(affich_gui,text = "Fermer",height = 18, width = 10, bg='dark slate gray',fg='azure2',font = "Verdana 10 bold",command = close)
    fermer.place(x=485,y=2)
    

def chercher():
    chercher_gui=Toplevel(app)
    chercher_gui.geometry("500x500")
    chercher_gui.title("Chercher un contact")
    photo_5 = PhotoImage(file = "chercher.png")
    chercher_gui.iconphoto(False, photo_5)
    chercher_gui['bg'] = 'dark slate gray'

    bloc1 = Canvas(chercher_gui, width=500, height=50, bg='dark slate gray')
    bloc2 = Canvas(chercher_gui, width=500, height=450, bg='dark slate gray')
    bloc3 = Canvas(chercher_gui, width=500, height=450, bg='dark slate gray')
    bloc1.place(x=0,y=0)
    bloc3.place(x=0,y=51)
    def search():        
        test_name = 0
        filtre = nom.get(1.0, END+"-1c")
        if filtre=='':
            Warning_lbl.configure(text="Donnez le nom du contact à afficher!")
            bloc2.place_forget()
            bloc3.place(x=0,y=51)
        else:
            file = open('contact.txt','r')
            data = file.readlines()
            for l in data:
                d=l.split('          ')
                n=d[0].split('  ')
                m=n[0]+' '+n[1]
                if n[0]==filtre:
                    test_name = 1
                    cherch_nom_label.configure(text='Nom: '+n[0])
                    cherch_prenom_label.configure(text='Prenom: '+n[1])
                    cherch_num_label.configure(text='Numero: '+d[1])
                    cherch_adr_label.configure(text='Adresse: '+d[2])
                    cherch_pic_label_2.configure(text='Photo: '+d[3])
                    break
            file.close()
            if test_name == 1:
                bloc3.place_forget()
                bloc2.place(x=0,y=51)
            else:
                Warning_lbl.configure(text="Contact Introuvable!")
                bloc2.place_forget()
                bloc3.place(x=0,y=51)
                      
    def fermer():
        chercher_gui.destroy()
        
    nom_label=Label(bloc1, text="Nom",bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    nom_label.place(x=20 ,y=20)
    nom=Text(bloc1, height = 1, width = 20)
    nom.place(x=80 ,y=20)
    search = ttk.Button(bloc1,text = "Chercher",command = search)
    search.place(x=300,y=5)
    ferm= ttk.Button(bloc1,text = "Fermer",command = fermer)
    ferm.place(x=400,y=5)

    cherch_nom_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    cherch_nom_label.place(x=20 ,y=20)
    cherch_prenom_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    cherch_prenom_label.place(x=20 ,y=90)
    cherch_num_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    cherch_num_label.place(x=20 ,y=160)
    cherch_adr_label=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    cherch_adr_label.place(x=20 ,y=230)
    cherch_pic_label_2=Label(bloc2,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    cherch_pic_label_2.place(x=20 ,y=300)
    division_label=Label(bloc2,text='-------------------------------------------------------------------',bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    division_label.place(x=0 ,y=330)
    
    Warning_lbl=Label(bloc3,bg='dark slate gray',fg='azure2',font = "Verdana 10 bold")
    Warning_lbl.place(x=150 ,y=20)


def closing():
    app.destroy()

style = ttk.Style()
style.configure('TButton', foreground='black', relief='raised', padding=10)

Button_ajout = ttk.Button(app,text = "Ajouter",command = ajouter )
Button_ajout.place(x=30,y=50  )

Button_supp = ttk.Button(app,text = "Supprimer"  ,command = supprimer)
Button_supp.place(x=140,y=100)

Button_modif = ttk.Button(app,text = "Modifier",command = modifier)
Button_modif.place(x=250,y=150)

Button_affich = ttk.Button(app,text = "Afficher",command = afficher)
Button_affich.place(x=360,y=200)

Button_cherch = ttk.Button(app,text = "Chercher",command = chercher)
Button_cherch.place(x=470,y=250)

Button_fermer = ttk.Button(app,text = "Fermer",command = closing)
Button_fermer.place(x=10,y=250)

app.mainloop()
