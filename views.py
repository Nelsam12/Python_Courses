from tabulate import tabulate

def display_product(list_product: list) -> None:
    data = [p for p in list_product]
    print(tabulate(data, tablefmt="rounded_grid"))

# def display_menu(msg: str):
#     print(msg)

def display_menu(list_items: list, start_count: int = 1, symb: str = "*", screen_width: int = 60) -> None:
    count = start_count
    element = "{" + f": ^{screen_width}" + "}"
    print(symb * screen_width)
    if isinstance(count, str):
        for titre in list_items:
            print(count, str(element).format(titre))
            count = chr(ord(count) + 1)
    else:
        for titre in list_items:
            print(count, str(element).format(titre))
            count += 1
    print(symb * screen_width)

def test_menu() -> None:
    print("1{:.>20}".format("Produit1")) # aligner à droite
    print("1{:.<20}".format("Produit1")) # aligner à gauche
    print("1{:.^20}".format("Produit1"))

def make_title(titres: list, symb: str = "*", screen_width: int = 75) -> None:
    print(symb*screen_width)
    for titre in titres:
        print("{:^75}".format(titre))
    print(symb*screen_width)


