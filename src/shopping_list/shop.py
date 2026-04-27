import sys
from storage import load_list, save_list
from utils import count_units, calc_line_total, calc_grand_total

def add_item(items, name, qty, price):
    """
    Pievieno jaunu produktu sarakstam un saglabā izmaiņas failā.
    
    Args:
    items(list): Esošais iepirkumu saraksts.
    name(str): Produkta nosaukums.
    qty(float): Produkta daudzums.
    price(str/float): Produkta cena.
    
    Returns:
    None
    """
    new_item = {"name": name, "qty": qty, "price": price}
    items.append(new_item)
    save_list(items)
    line_total = calc_line_total(new_item)
    print(f"✓ Pievienots: {name} x {qty} ({float(price):.2f} EUR/gab.) = {line_total:.2f} EUR")

    # ✓ Pievienots: Maize × 3 (1.20 EUR/gab.) = 3.60 EUR

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
        line_total = calc_line_total(item)
        print(f"  {i}. {item['name']} x {item['qty']} - {float(item['price']):.2f} EUR/gab. - {line_total:.2f} EUR")

        # 1. Maize × 3 — 1.20 EUR/gab. — 3.60 EUR

def main():
    items = load_list()                 # Izsaucam datu ielādes funkciju

    # Pārbaudām, vai ir ievadīta komanda (add vai list)
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add|list|total|clear]")
        return

    command = sys.argv[1].lower()    

    if command == "add" and len(sys.argv) == 5:
        name = sys.argv[2]
        qty = sys.argv[3] 
        price = sys.argv[4] 
        add_item(items, name, qty, price)       # Izsaucam pievienošanas funkciju  

    elif command == "list":
        show_list(items)        # Izsaucam izvades funkciju

    elif command == "total":
        total_amount = calc_grand_total(items)
        count = len(items)
        count_items = count_units(items)
        print(f"Kopā: {total_amount:.2f} EUR ({count_items} vienības, {count} produkti)")

        # Kopā: 6.60 EUR (5 vienības, 2 produkti)

    elif command == "clear":
        items = []              # Izveidojam tukšu sarakstu
        save_list(items)        # Saglabājam tukšo sarakstu, tādējādi izdzēšot veco saturu
        print("✓ Iepirkumu saraksts ir notīrīts.")


if __name__ == "__main__":
    main()

