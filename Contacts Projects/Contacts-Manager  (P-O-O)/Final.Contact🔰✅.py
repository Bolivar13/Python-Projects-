import csv


class Contact():
    
 def __init__(self, nom_complet , email, tel, adress, number=0):
        
        self.id= number
        self.nom_complet = nom_complet
        self.email = email
        self.tel= tel
        self.adress=adress


FILENAME = "contacts-book.csv"

# ------------------------------

def voir_cc_csv():
    try:
        contacts = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    except FileNotFoundError as e:
       print("INVALIDE " + FILENAME + " file.")
       f=open(FILENAME, "w+")

       return contacts
    except Exception as e:
        print(type(e), e)

# ------------------

def ajouter_cc_csv(contacts):
    try:
        with open (FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

    except OSError as e:
        print(type(e), e)

    except Exception as e:
        print(type(e), e)
 
# -----------------------

def list_contacts(contacts):
        for i in range(0, len(contacts)):
           contact = contacts[i]
           print(str(i+1) + ". " + contact[0]+ "(" + str(contact[1]) +")" )
           print()
        
# -----------------------

def ajouter_contacts(contacts):
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
    ajouter_cc_csv(contacts)
    print(name + " Est Ajouter")
    print()

# ------------------

def supprimer_contacts(contacts):

    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer.")
            continue


        if number < 0 or number > len (contacts):
            print()


        else:
           break
        contact = contacts.pop(number-1)
        ajouter_cc_csv(contacts)
        print(contact[0] + " \nEst Supprimer")

# -------------------

def afficher_menu():
    
    print("MENU :")

    print("Saisir une Choix ")
    print()
    print("\nadd - Ajouter un contact",
          "\ndel - Supprimer un contact",
          "\nlist - lister contacts",  
          "\nexit - Quitter !!")

    print()

# ------------------------

def main():


    afficher_menu()
    contacts =  voir_cc_csv()
    while True:
        command = input("Entrer Votre Choix 🔰 : ")

        if command.lower() == "add":
            ajouter_contacts(contacts)

        elif command.lower() == "del":
            supprimer_contacts(contacts)

        elif command.lower() == "list":
            list_contacts(contacts)
    
        elif command.lower() == "exit":
            print("Au revoir!")
            break
        else:
            print("Invalide Choix !!.\n")



if __name__ == "__main__":
    main()
    