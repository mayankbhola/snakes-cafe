from collections import OrderedDict

menu_header = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

menu_footer = """***********************************
** What would you like to order? **
***********************************"""

menu_delimeter = """
----------"""

order_header = """
***********************************
** Thanks for your order **
"""

order_footer = """***********************************
"""

# To maintain orfer of menu
menu = OrderedDict([
        ("Appetizers" , ["Wings", "Cookies", "Spring Rolls"]),
        ("Entrees" , ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]),
        ("Desserts" , ["Ice Cream", "Cake", "Pie"]),
        ("Drinks" , ["Coffee", "Tea", "Unicorn Tears"])
    ])


order = OrderedDict()