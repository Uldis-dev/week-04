import os
import json

def load_list(shopping_file="shopping.json"):
    """
    Nolasa iepirkumu sarakstu no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu.
    
    Args:
    shopping_file(str): Ceļš līdz JSON failam, kurā glabājas iepirkumu saraksts.
    
    Returns:
    list: Iepirkumu saraksts (saraksts ar vārdnīcām) vai [] ja fails neeksistē.

    Example:
    >>> load_list('neeksistejos_fails.json')
    []
    >>> load_list('shopping.json')
    [{"name": "Maize", "price": 1.20}]
    """
    if not os.path.exists(shopping_file):
        return []   # ja fails nav, atgriež tukšu sarakstu
    
    try:
        with open(shopping_file, 'r', encoding='utf-8') as file:
            return json.load(file)     #ielasa faila saturu atmiņā
    except (json.JSONDecodeError, IOError):
        # Ja fails ir bojāts vai to nevar nolasīt, atgriežam tukšu sarakstu
        return []        
        

def save_list(shopping_list, shopping_file="shopping.json"):
    """
    Saglabā iepirkumu sarakstu JSON failā, izmantojot UTF-8 kodējumu.
    
    Args:
    shopping_list(list): Saraksts ar vārdnīcām, ko nepieciešams saglabāt.
    shopping_file(str): Ceļš līdz JSON failam, kurā dati tiks ierakstīti.
    
    Returns:
    None: Funkcija datus tikai ieraksta failā un vērtību neatgriež.
    """    
    with open(shopping_file, 'w', encoding='utf-8') as file:
        json.dump(shopping_list, file, ensure_ascii=False, indent=4) #pārveido json formātā    


if __name__ == "__main__":
    # Šis bloks kalpo tikai ātrai pašpārbaudei
    test_data = [{"name": "Testa Maize", "price": 1.50}]
    save_list(test_data, "test.json")
    print("Dati saglabāti test.json")
    print("Ielādētie dati:", load_list("test.json"))