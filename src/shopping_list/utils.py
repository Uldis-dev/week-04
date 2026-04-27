def count_units(items):
    """
    Saskaita kopējo vienību skaitu (summē visus qty).
    Ignorē negatīvas vērtības un kļūdainus datus.
    """
    total_units = 0
    for item in items:
        try:
            qty = int(item.get('qty', 1))           # Iegūstam qty, ja tā nav, pieņemam 1
            
            if qty > 0:                 # Pieskaitām tikai tad, ja daudzums ir pozitīvs
                total_units += qty
        except (ValueError, TypeError):
            continue                 # Ja dati ir "slikti", šo rindu vienkārši izlaižam
            
    return total_units


def calc_line_total(item):
    """
    Atgriež vienas rindas kopsummu (daudzums x cena).
    Nodrošina, ka cena un daudzums nav negatīvi.
    Ja dati ir kļūdaini vai negatīvi, atgriež 0.0.
    """
    try:
        price = float(item.get('price', 0))
        qty = int(item.get('qty', 1))

        if price < 0 or qty < 0:        # Pārbaude: ja kāda no vērtībām ir negatīva, uzskatām to par 0
            return 0.0

        return price * qty
    except (ValueError, TypeError):
        return 0.0
    

def calc_grand_total(items):
    """
    Summē visus line totals no iepirkumu saraksta.
    """
    grand_total = 0.0
    for item in items:
        grand_total += calc_line_total(item)
    return grand_total

