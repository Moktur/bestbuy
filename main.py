from products import Product
from store import Store
from constants import STARS, LIST_OF_COLORS_MENU, LIST_OF_FONT_COLORS, RESET


def print_colored(text, color_code):
    """Print the given text in the specified color."""
    print(f"{color_code}{text}{RESET}")


def start(store:Store):
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


    product_list = [
                Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
