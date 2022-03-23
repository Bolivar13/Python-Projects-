import csv

fields = ['Name', 'Contact Number'  , 'Email' , 'Address']

file = open("contacts-Book.csv", 'w')
x = int(input("Combien de contacts voulez-vous enregistrer ⚠ ? "))

writer = csv.writer(file)
writer.writerow(fields)

for i in range(0, x):
    name = input("Enter Contact Name: ")
    number = input("Enter Votre Numero: ")
    Email = input("Entrer Votre Email : ")
    Address = input("Entrer Votre Address : ")
    a = []

    a.append(name)
    a.append(number)
    a.append(Email)
    a.append(Address)

    writer.writerow(a)
    
if a :
    print("votre contact est créé ...!!✅")
else:
    print("no")
file.close()