class Product:
    """
    Represents a single product in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price per unit of the product.
        quantity (int): The current available quantity of the product.
        active (bool): Indicates whether the product is available for purchase.
    """

    def __init__(self, name, price, quantity, active=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("No negative or empty values allowed")


    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        Returns:
            int: The available quantity.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Sets a new quantity for the product.

        Args:
            quantity (int): The new quantity to be set.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactive()


    def is_active(self) -> bool:
        """
        Indicates whether the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """
        Sets the product status to active.
        """
        self.active = True


    def deactive(self):
        """
        Sets the product status to inactive.
        """
        self.active = False


    def show(self):
        """
        Returns a string representation of the product with its name, price, and quantity.

        Returns:
            str: A formatted product string.
        """
        if self.is_active():
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity:float) -> float:
        """
        Attempts to buy a certain quantity of the product.

        If the requested quantity exceeds available stock, prints an error and returns None.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float | None: The total price if successful, otherwise None.
        """
        if quantity > self.quantity:
            print(
                f"Only {self.quantity} left of {self.name}."
                f" You need to pick {quantity - self.quantity} unit(s) less."
                )
            return None
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactive()
        return quantity * self.price
