from contact import Contact
class Contact_List:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Name\tEmail\tTelephone")
            print("-" * 40)
            for contact in self.contacts:
                print(contact)
