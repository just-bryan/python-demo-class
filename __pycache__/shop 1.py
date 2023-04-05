import utils
from pprint import pprint
last_index = 0

PRODUCTS_DB = utils.get_products()



def view_products():
    global last_index
    next_index =last_index + 2
    pprint(PRODUCTS_DB[last_index:next_index])
    last_index = next_index
    
    while True:
        print("1) view products")
        cmd = input("type here>> ")
        if cmd == "1":
            view_products()
        else:
            break

        