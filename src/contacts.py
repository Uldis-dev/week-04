import sys
import os
import json

#
def load_contacts(contacts_file="contacts.json"):
    if not os.path.exists(contacts_file):
        return []   # ja fails nav, atgriež tukšu sarakstu
    with open(contacts_file, 'r', encoding='utf-8') as file:
        return json.load(file)     #ielasa faila saturu atmiņā
    
def save_contacts(saraksts_ar_kontaktiem, contacts_file="contacts.json"):
    with open(contacts_file, 'w', encoding='utf-8') as file:
        json.dump(saraksts_ar_kontaktiem, file, ensure_ascii=False, indent=2) #pārveido json formātā

def add_contact(contact_list):
    name = input("Ievadiet kontakta vārdu: ")
    phone = input("Ievadiet telefona numuru: ")
    contact_list.append({"name": name, "phone": phone})
    print(f"Kontakts '{name}' ir pievienots.")
    return True

if __name__ == "__main__":
    contact_list = load_contacts()
    add_contact(contact_list)
    save_contacts(contact_list)

