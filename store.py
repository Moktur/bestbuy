from products import Product


class Store:
    """
    Represents the store containing a list of products.

    Attributes:
        list_of_products (list[Product]): A list of all products available in the store.

    Methods:
        add_product(product): Adds a new product to the store.
        remove_product(product): Removes a product from the store.
        get_total_quantity(): Returns the total quantity of all products in the store.
        get_all_products(): Returns a list of active products only.
        order(shopping_list): Processes a list of
        product-quantity pairs and returns the total price.
    """

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products


    def add_product(self, product):
        """
        Adds a new product to the store.

        Args:
            product (Product): The product to add.
        """
        self.list_of_products.append(product)


    def remove_product(self, product):
        """
        Removes a product from the store if it exists.

        Args:
            product (Product): The product to remove.
        """
        for item in self.list_of_products:
            if item == product:
                self.list_of_products.remove(item)


    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: Total quantity of all items.
        """
        quantity = 0
        for item in self.list_of_products:
            quantity += item.get_quantity()
        return quantity


    def get_all_products(self) -> list[Product]:
        """
        Returns a list of all active products.

        Returns:
            list[Product]: List of products that are currently active.
        """
        active_items = []
        for item in self.list_of_products:
            if item.is_active():
                active_items.append(item)
        return active_items


    def order(self, shopping_list) -> float:
        """
        Processes a shopping list and returns the total cost.

        If any product cannot fulfill the requested quantity, aborts the order and returns None.

        Args:
            shopping_list (list[tuple[Product, int]]): A list of (Product, quantity) pairs.

        Returns:
            float | None: Total price if successful, otherwise None.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            if price is None:
                return None
            total_price += price
        return total_price
