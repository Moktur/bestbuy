class Product:
    def __init__(self, name, price, quantity, active=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("No negative or empty values allowed")
     
     
    def get_quantity(self) -> int:
        """returns the quantity of the product"""
        return self.quantity


    def set_quantity(self, quantity):
        """set a new quantity"""
        self.quantity = quantity


    def is_active(self) -> bool:
        """returns a boolean if the product is active or not"""
        return self.active


    def activate(self):
        """activates the product"""
        self.active = True


    def deactive(self):
        """deactive the product"""
        self.active = False


    def show(self):
        """
        returns a string of showing the name, 
        price and quantity of the product
        """
        return (f"{self.name}, Price: {self.price}, Quantitiy: {self.quantity}")


    def buy(self, quantity:float) -> float:
        """
        returns the total price of ordered product and quantity.
        If the ordered quantity is to high, it will return None
        """
        if quantity > self.quantity:
            print(
                f"Only {self.quantity} left of {self.name}."
                f" You need to pick {quantity - self.quantity} unit(s) less."
                )
            return None
        else:
            self.quantity -= quantity
            return quantity * self.price
