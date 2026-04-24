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

def add_contact_argv(contact_list, name, phone):
    """
    Paņem funkcijas inputā saņemtos kontakta datus un pievieno jaunu kontaktu sarakstam.
    
    Args:
    contact_list(list): Esošais kontaktu saraksts (saraksts ar vārdnīcām).
    name 
    phone
    
    Returns:
    bool: True pēc veiksmīgas kontakta pievienošanas.
    """    
    contact_list.append({"name": name, "phone": phone})
    print(f"✓ Pievienots: {name} ({phone})")
    return True

def list_contacts(contacts_list):
    """
    Izvada visus kontaktus sarakstā.
    
    Args:
    contact_list(list): Esošais kontaktu saraksts (saraksts ar vārdnīcām).

    Returns:
    list: Visi kontakti vienā sanummurētā sarakstā    
    """
    if not contacts_list:
        print("Kontaktu saraksts ir tukšs.")
        return
    print("Kontakti:")
    for i, contact in enumerate(contacts_list, 1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")

def search_contacts(contacts_list, name):
    """Meklē kontaktus pēc vārda daļas (reģistrnejūtīgi)."""
    found = [c for c in contacts_list if name.lower() in c['name'].lower()]
    
    if not found:
        print(f"Netika atrasts neviens kontakts, kas satur '{name}'.")
    else:
        print(f"Atrasti {len(found)} kontakti:")
        for i, contact in enumerate(found, 1):
            print(f"  {i}. {contact['name']} — {contact['phone']}")        


if __name__ == "__main__":
    # 1. Pārbaude, vai ir ievadīti komandrindas argumenti
    if len(sys.argv) < 2:
        print("Lietošana: python contacts.py [add|list|search] [dati]")
        sys.exit(1)
    command = sys.argv[1].lower()

  # 2. Ielādējam datus
    contact_list = load_contacts()
    
    # 3. Komandas
    if command == "add":
        if len(sys.argv) == 4:
            name = sys.argv[2]
            phone = sys.argv[3]
            add_contact_argv(contact_list, name, phone)
            save_contacts(contact_list)
        else:
            print("Kļūda: Jānorāda vārds un tālrunis. Piemērs: python contacts.py add 'Vārds' '1234'")

    elif command == "list":
        list_contacts(contact_list)

    elif command == "search":
        if len(sys.argv) == 3:
            name = sys.argv[2]
            search_contacts(contact_list, name)
        else:
            print("Kļūda: Norādiet meklējamo vārdu. Piemērs: python contacts.py search Anna")
    
    else:
        print(f"Nezināma komanda: {command}")  