import sys
from storage import load_list, save_list, load_prices, save_prices, get_price, set_price
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

    if command == "add" and len(sys.argv) >= 3:
        name = sys.argv[2]
        # --- DAUDZUMA PĀRBAUDE ---
        try:
            qty = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            if qty <= 0:
                print("Kļūda: Daudzumam jābūt lielākam par 0! Iestatīts uz 1.")
                qty = 1
        except ValueError:
            print("Kļūda: Daudzumam jābūt veselam skaitlim! Iestatīts uz 1.")
            qty = 1

        price = get_price(name)

        if price is not None:
            # Scenārijs: JĀ, cena ir atrasta
            print(f"Precei '{name}' atrasta cena: {price:.2f} EUR")
            choice = input("[A]kceptēt vai [M]ainīt? ").lower()
            
            if choice == 'm':
                while True: # Cikls, kamēr ievadīs pareizi
                    try:
                        new_price = float(input(f"Ievadi jaunu cenu: ").replace(',', '.'))
                        if new_price > 0:
                            price = new_price
                            set_price(name, price)
                            print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")
                            break
                        print("Kļūda! Cenu nevar iestatīt uz 0 vai negatīvu!")
                    except ValueError:
                        print("Kļūda! Lūdzu, ievadiet skaitli!")
        else:
            while True:
                try:
                    print(f"Cena precei '{name}' nav zināma.")
                    new_price = float(input(f"Ievadi cenu: ").replace(',', '.'))
                    if new_price > 0:
                        price = new_price
                        set_price(name, price)
                        print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")
                        break
                    print("Kļūda! Cenai jābūt lielākai par 0!")
                except ValueError:
                    print("Kļūda! Lūdzu, ievadiet skaitli!")    
 
        add_item(items, name, qty, price)       # Izsaucam pievienošanas funkciju  

    elif command == "list":
        show_list(items)        # Izsaucam izvades funkciju

    elif command == "total":
        total_amount = calc_grand_total(items)
        count = len(items)
        count_items = count_units(items)
        print(f"Kopā: {total_amount:.2f} EUR ({count_items} vienības, {count} produkti)")

    elif command == "clear":
        items = []              # Izveidojam tukšu sarakstu
        save_list(items)        # Saglabājam tukšo sarakstu, tādējādi izdzēšot veco saturu
        print("✓ Iepirkumu saraksts ir notīrīts.")


if __name__ == "__main__":
    main()

