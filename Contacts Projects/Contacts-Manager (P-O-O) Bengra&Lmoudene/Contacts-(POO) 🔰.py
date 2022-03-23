import csv
 


class Contact():
    
 def __init__(self, nom_complet , email, tel, Adress, id=0):
        
        self.id= id
        self.nom_complet = nom_complet
        self.email = email
        self.tel= tel
        self.Adress=Adress


FILENAME = "contacts.csv"


def Chercher_contacts():
    try:
        contacts = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    except FileNotFoundError as e:
       print("N'a pas trouver " + FILENAME + " file.")
       f=open(FILENAME, "w+")

       return contacts
    except Exception as e:
        print(type(e), e)
 



  


def list_contacts(contacts): 
     
        for i in range(0, len(contacts)):
           contact = contacts[i]
           print(str(i+1) + ". " + contact[0]+ "(" + str(contact[1]) +")" )
           print()


def Afficher_contacts(contacts):
    while True:
        try:
            number  = int(input("ID: "))


        except ValueError:
            print("Invalide ID")
            continue



def Ajouter_contacts(contacts):
    name = input("Saisir Votre Nom Complet: ")
    email = input("Saisir Votre  Email: ")
    phone = input("Saisir Votre Telephone: ")
    adress = input("Saisir Votre Adress:")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact.append(adress)
    contacts.append(contact)
    print(name + " Est Ajouter !!")
    print()


def Supprimer_contacts(contacts):
    while True:
        try:
            number = int(input("ID: "))
        except ValueError:
            print("Invalide.")
            continue


        if number < 0 or number > len (contacts):
            print("invalid !!")


        else:
           break

        contact = contacts.pop(number-1)
        print(contact[0] + " Est Supprimer !!")



def Afichage_menu():

    print("Entrer un Choix:")
    print()
    print("list - Afficher list contacts", "\nview - Voir contact",
          "\nadd - Ajouter contact", "\ndel - Supprimer contact",
          "\nexit - Quitter program")

    print()


def main():


    Afichage_menu()

    contacts =  Chercher_contacts()

    while True:
        command = input("Entrer Un choix : ")

        if command.lower() == "list":
            list_contacts(contacts)

        elif command.lower() == "view":
            Afficher_contacts(contacts)

        elif command.lower() == "add":
            Ajouter_contacts(contacts)

        elif command.lower() == "del":
            Supprimer_contacts(contacts)

        elif command.lower() == "exit":
            print("Au revoir !!")
            break

        else:
            print("Invalid Choix !!.\n")

if __name__ == "__main__":
    main()