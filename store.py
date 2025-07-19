from products import Product

class Store:
    
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products


    def add_product(self, product):
        self.list_of_products.append(product)


    def remove_product(self, product):
        for item in self.list_of_products:
            if item == product:
                self.list_of_products.remove(item)


    def get_total_quantity(self) -> int:
        quantity = 0
        for item in self.list_of_products:
            quantity += item.get_quantity()
        return quantity

    def get_all_products(self) -> list[Product]:
        active_items = []
        for item in self.list_of_products:
            if item.is_active():
                active_items.append(item)
        return active_items


    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price