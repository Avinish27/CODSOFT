import json

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        self.save_contacts()

    def view_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

    def search_contact(self, keyword):
        results = [c for c in self.contacts if keyword in c["name"] or keyword in c["phone"]]
        return results

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact["name"] == name:
                if new_phone:
                    contact["phone"] = new_phone
                if new_email:
                    contact["email"] = new_email
                if new_address:
                    contact["address"] = new_address
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c["name"] != name]
        self.save_contacts()

contact_book = ContactBook()
contact_book.add_contact("John Doe", "1234567890", "john@example.com", "123 Street Name")
contact_book.view_contacts()
search_result = contact_book.search_contact("John")
print(search_result)
contact_book.update_contact("John Doe", new_phone="0987654321")
contact_book.view_contacts()
contact_book.delete_contact("John Doe")
contact_book.view_contacts()
