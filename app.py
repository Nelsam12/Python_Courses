from const import *
from functions import *
from views import *
from datetime import *

# os.mkdir("./FacturesPDF")
rep = "OUI"
panier = []
# somme = 0
all_products = get_file_content(PRODUCT_FILE)
all_sale = get_file_content(SALE_FILE)
available_products = get_available_products(all_products)
my_cart = get_file_content(PANIER)
line_command = get_file_content(COMMAND_LINE)
main_loop(panier, available_products)

# Menu principal
traitement(panier, all_products, available_products)


print("Fin du projet !")