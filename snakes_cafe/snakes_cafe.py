from snakes_cafe.menu_info import menu, menu_header, menu_footer, menu_delimeter
from snakes_cafe.menu_info import order, order_header, order_footer


def print_menu() :
    for category, items in menu.items() :
        print(f"{category}{menu_delimeter}")
        print(*items, sep = "\n")
        print()


def display_menu():
    print(menu_header)
    print_menu()
    print(menu_footer)


def validate(item) :
    for items in menu.values() :
        if item.title() in items :
            return True
    
    return False


def process(item) :
    if not validate(item) :
        raise Exception(f"\n** Sorry, Item :: {item.title()} doesn't exist in menu **\n")
    
    if item not in order.keys() :
        order[item] = 1
    else :
        order[item] += 1

    print(f"\n** {order[item]} order of {item.title()} have been added to your meal **\n")


def dump_order() :
    print(order_header)
    
    if not order.keys() :
        print(f"** Sorry, Your meal is empty. **")
    else :
        for item in order.keys() :
            print(f"** {order[item]} order of {item.title()} have been added to your meal **")
    print(order_footer)


def init():
    display_menu()
    item = input().lower()

    while item != "quit" :
        try :
            process(item)
        except Exception as error :
            print(error)
        item = input().lower()
    
    dump_order()


if __name__ == "__main__":
    init()
