import utils
from pprint import pprint
last_index =0
PRODUCTS_DB= utils.get_products


def view_products ():
    global last_index
    # global means if you want to acces a global variable outside a fuction you need to call it using global and the global variable
    next_index = last_index + 2
    pprint(PRODUCTS_DB[last_index:next_index], indent=4)
    last_index = next_index
    
while True:
    print("1) view products")
    cmd =input("type here >>>")
    if cmd == "1":
        view_products()
    else:
        break
            