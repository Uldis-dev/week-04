import sys
import os
import json

#
def load_contacts(contacts_file="contacts.json"):
    """
    Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu.
    
    Args:
    contacts_file(str): Ceļš līdz JSON failam, kurā glabājas kontakti.
    
    Returns:
    list: Kontaktu saraksts (saraksts ar vārdnīcām) vai [] ja fails neeksistē.

    Example:
    >>> load_contacts('neeksistejos_fails.json')
    []
    >>> load_contacts('contacts.json')
    [{'name': 'Anna', 'phone': '123'}]
    """
    if not os.path.exists(contacts_file):
        return []   # ja fails nav, atgriež tukšu sarakstu
    with open(contacts_file, 'r', encoding='utf-8') as file:
        return json.load(file)     #ielasa faila saturu atmiņā
    
def save_contacts(contacts_list, contacts_file="contacts.json"):
    """
    Saglabā kontaktu sarakstu JSON failā, izmantojot UTF-8 kodējumu.
    
    Args:
    contacts_list(list): Saraksts ar vārdnīcām, ko nepieciešams saglabāt.
    contacts_file(str): Ceļš līdz JSON failam, kurā dati tiks ierakstīti.
    
    Returns:
    None: Funkcija datus tikai ieraksta failā un vērtību neatgriež.
    """    
    with open(contacts_file, 'w', encoding='utf-8') as file:
        json.dump(contacts_list, file, ensure_ascii=False, indent=2) #pārveido json formātā

def add_contact(contact_list):
    """
    Pieprasa lietotājam ievadīt datus un pievieno jaunu kontaktu sarakstam.
    
    Args:
    contact_list(list): Esošais kontaktu saraksts (saraksts ar vārdnīcām).
    
    Returns:
    bool: True pēc veiksmīgas kontakta pievienošanas.

    Example:
    >>> kontakti = []
    >>> add_contact(kontakti)
    Ievadiet kontakta vārdu: Anna
    Ievadiet telefona numuru: 26123456
    Kontakts 'Anna' ir pievienots.
    True
    """    
    name = input("Ievadiet kontakta vārdu: ")
    phone = input("Ievadiet telefona numuru: ")
    contact_list.append({"name": name, "phone": phone})
    print(f"Kontakts '{name}' ir pievienots.")
    return True

if __name__ == "__main__":
    contact_list = load_contacts()
    add_contact(contact_list)
    save_contacts(contact_list)

