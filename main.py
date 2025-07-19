from products import Product
from store import Store

YELLOW = "\033[103m"
MAGENTA = "\033[45m"
CYAN = "\033[106m"
GREEN = "\033[102m"
RESET = "\033[0m"
LIST_OF_COLORS = [YELLOW, MAGENTA, CYAN, GREEN]


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
        i = 0
        for i in range(len(MENU_OPTIONS)):
            print_colored(MENU_OPTIONS[i], LIST_OF_COLORS[i])
            # print_colored(option, COLOR_MENU)
        # TODO: Try Except
        user_input = int(input("Please choose a number: "))
        if user_input == 1:
            numerical_list_of_all_products(store)
        if user_input == 2:
            print(f"Total of {store.get_total_quantity()} items in the store")
        if user_input == 3:
            numerical_list_of_all_products(store)
            make_order(store)
        if user_input == 4:
            break


def numerical_list_of_all_products(store):
    length = len(store.get_all_products())
    counter = 1
    for product in store.get_all_products():
        print(f"{counter}. {product.show()}")
        counter += 1

def make_order(store):
    shopping_list = []
    while True:
        print("When you want to finish the order, enter an empty text")
        # TODO: Try and Except
        product_number = input("Which product # do you want? ")
        quantity = input("What amount do you want? ")
        if product_number == "" and quantity == "":
            print(f"Total price: {store.order(shopping_list)}")
            break
        else:
            try:
                product_number = int(product_number)
                quantity = int(quantity)
            except Exception as e:
                print(f"{e}: Can't transform value into number, use a normal number")
            product_list = store.get_all_products()
            product = product_list[product_number - 1]
            # TODO: Try Except
            shopping_list.append((product, quantity))
            

  

def main():
    # bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    # mac = Product("MacBook Air M2", price=1450, quantity=100)

    # print(bose.buy(50))
    # print(mac.buy(100))
    # print(mac.is_active())

    # bose.show()
    # mac.show()

    # bose.set_quantity(1000)
    # bose.show()

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)


    start(best_buy)

if __name__ == "__main__":
    main()