class Product:
    def __init__(self, name, price, quantity, active=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("No negative or empty values allowed")
     
     
    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactive(self):
        self.active = False


    def show(self):
        return (f"{self.name}, Price: {self.price}, Quantitiy: {self.quantity}")


    def buy(self, quantity:float) -> float:
        if quantity > self.quantity:
            raise ValueError(
                f"Only {self.quantity} left."
                f" You need to pick {quantity - self.quantity} units less."
                )
        else:
            self.quantity -= quantity
        return quantity * self.price
        # TODO: Nachfrage beim User ob er die mögliche Anzahl an Bestellung machen will.