from products import Product
from store import Store

STARS = "☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆\n"
YELLOW = "\033[103m"
MAGENTA = "\033[45m"
CYAN = "\033[106m"
GREEN = "\033[102m"
RESET = "\033[0m"
LIST_OF_COLORS_MENU = [YELLOW, MAGENTA, CYAN, GREEN]

FONT_MAGENTA = "\033[35m"
FONT_CYAN = "\033[36m"
FONT_BRIGHT_BLACK = "\x1b[90m"
LIST_OF_FONT_COLORS = [FONT_MAGENTA, FONT_CYAN, FONT_BRIGHT_BLACK]


def print_colored(text, color_code):
    """
    Prints the given text to the console with the specified ANSI color code.

    Args:
        text (str): The text to display.
        color_code (str): The ANSI escape code for the color.
    """
    print(f"{color_code}{text}{RESET}")


def start(store:Store):
    """
    Starts the main interactive menu loop for the store.

    Displays options to list products, show total quantity, make an order,
    or quit the application. Handles user input and calls corresponding
    helper functions.

    Args:
        store (Store): The store object to operate on.
    """
    MENU_OPTIONS = [
        "1. List all products in the store",
        "2. Show total amount in the store",
        "3. Make an order",
        "4. Quit"
        ]

    while True:
        print("\n🛒 Store Menu 📺 ")
        print_colored(STARS, LIST_OF_FONT_COLORS[2])
        i = 0
        for i in range(len(MENU_OPTIONS)):
            print_colored(MENU_OPTIONS[i], LIST_OF_COLORS_MENU[i])
        try:
            user_input = int(input("Please choose a number: "))
            if user_input == 1:
                numerical_list_of_all_products(store)
            if user_input == 2:
                print(f"Total of {store.get_total_quantity()} items in the store\n")
                print_colored(STARS, LIST_OF_FONT_COLORS[2])
            if user_input == 3:
                numerical_list_of_all_products(store)
                make_order(store)
            if user_input == 4:
                break
        except ValueError as e:
            print("Please enter a number from 1-4. Try again.")


def numerical_list_of_all_products(store):
    """
    Displays all active products in the store in a numbered list.

    Alternates text color for better visibility.

    Args:
        store (Store): The store object containing the products.
    """
    length = len(store.get_all_products())
    counter = 1
    set_color = 0
    print_colored(STARS, LIST_OF_FONT_COLORS[2])
    for product in store.get_all_products():
        print_colored(
            f"{counter}. {product.show()}",
            LIST_OF_FONT_COLORS[set_color]
            )
        counter += 1
        # iterating with colors
        if set_color == 0:
            set_color = 1
        else:
            set_color = 0
    print_colored(STARS, LIST_OF_FONT_COLORS[2])


def make_order(store):
    """
    Allows the user to create an order by selecting products and quantities.

    Users can add multiple products to the shopping list. When they finish,
    the order is processed and the total price is displayed.
    If any requested quantity exceeds availability, the process is aborted.

    Args:
        store (Store): The store where products are purchased.
    """
    shopping_list = []
    print("When you want to finish the order, enter an empty text")
    while True:
        product_number = input("Which product # do you want? ")
        quantity = input("What amount do you want? ")
        if product_number == "" and quantity == "":
            # calculated_price can be None if ordered quantity > store quantity
            calculated_price = store.order(shopping_list)
            if calculated_price is None:
                break
            else:
                print(f"Total price: 💲{calculated_price}")
                break
        else:
            try:
                product_number = int(product_number)
                quantity = int(quantity)
                product_list = store.get_all_products()
                product = product_list[product_number - 1]
                shopping_list.append((product, quantity))
                print("Product added to the list.\n")
            except IndexError:
                print(
                    "This Product number is not listed. " \
                    "Please choose a valid Item number which is displayd in the list")
                continue
            except Exception as e:
                print(f"Can't transform value into number, use a normal number")
                continue


def main():
    """
    Entry point of the application.

    Initializes products, creates a store instance, and starts the menu system.
    """
    product_list = [
                Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
