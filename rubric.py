#Hier sollte Ihre Lösung stehen.
#Speichern Sie diese als .py-Datei und führen Sie das Programm auf der Konsole aus.
class Contact:
        def __init__ (self, name, phonenumber, email):
                self.name=name
                self.phonenumber=phonenumber
                self.email=email

        def display(self):
                return f"Name: {self.name}, PhoneNumber: {self.phonenumber}, Email: {self.email}"
        

class Rubric:
        def __init__(self):
                self.contacts=[]

        def createContact(self, contact):
                self.contacts.append(contact)
        
        def deleteContact(self, name):
                for contact in self.contacts:
                        if contact.name == name:
                                self.contacts.remove(contact)
                                print("The contact was found and deleted")
                                return
                print("Name not found!")
        
        def findContact(self,name_or_number):
                foundContacts=[]
                for contact in self.contacts:
                        if name_or_number in contact.name or name_or_number in contact.number:
                                foundContacts.append(contact)
                if foundContacts=="":
                        print("No contacts found")
                else:
                        print("Contacts found:")
                        for contact in foundContacts:
                                print(contact.display())
                        
        
        def editContact(self,name,new_name):
                for contact in self.contacts:
                        if contact.name == name:
                                contact.name=new_name
                                print("Contact is edited:")
                                print(contact.display())
                                return 
                print("Contact not found!")

        def display(self):
                for contact in self.contacts:
                        print(contact.display())

                        
contact1 = Contact("Dino", "1234", "abc")
contact2 = Contact("Mina", "12345", "abc")

rubric = Rubric()
rubric.createContact(contact1)
rubric.createContact(contact2)

rubric.display()

rubric.deleteContact("Dino")
rubric.display()
rubric.findContact("Mina")
rubric.editContact("Mina","Dinova Ljubav")