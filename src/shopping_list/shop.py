import sys
from storage import load_list, save_list

def add_item(items, name, price):
    """
    Pievieno jaunu produktu sarakstam un saglabā izmaiņas failā.
    
    Args:
    items(list): Esošais iepirkumu saraksts.
    name(str): Produkta nosaukums.
    price(str/float): Produkta cena.
    
    Returns:
    None
    """
    items.append({"name": name, "price": price})
    save_list(items)
    print(f"✓ Pievienots: {name} ({price}) EUR")

def show_list(items):
    """
    Izvada iepirkumu sarakstu terminālī.
    
    Args:
    items(list): Saraksts ar vārdnīcām (iepirkumiem).
    
    Returns:
    None
    """
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item['name']} - {item['price']} EUR")

def get_total(items):
    """
    Aprēķina visu sarakstā esošo produktu kopsummu.
    
    Args:
    items(list): Iepirkumu saraksts.
    
    Returns:
    float: Kopējā summa EUR.
    """
    total = 0.0
    for item in items:
        # Pārvēršam cenu par float, lai varētu saskaitīt
        # Ja 1. etapā cena ir teksts, šeit mēs to uz mirkli pārvēršam skaitlī
        try:
            total += float(item['price'])
        except ValueError:
            # Ja cena nav skaitlis, to ignorējam, lai programma nesalūztu
            continue
    return total

def main():
    items = load_list()                 # Izsaucam datu ielādes funkciju

    # Pārbaudām, vai ir ievadīta komanda (add vai list)
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add|list|total|clear]")
        return

    command = sys.argv[1].lower()    

    if command == "add" and len(sys.argv) == 4:
        name = sys.argv[2]
        price = sys.argv[3] 
        add_item(items, name, price)       # Izsaucam pievienošanas funkciju  

    elif command == "list":
        show_list(items)        # Izsaucam izvades funkciju

    elif command == "total":
        total_amount = get_total(items)
        count = len(items)
        print(f"Kopā: {total_amount:.2f} EUR ({count} produkti)")

    elif command == "clear":
        items = []              # Izveidojam tukšu sarakstu
        save_list(items)        # Saglabājam tukšo sarakstu, tādējādi izdzēšot veco saturu
        print("✓ Iepirkumu saraksts ir notīrīts.")


if __name__ == "__main__":
    main()

