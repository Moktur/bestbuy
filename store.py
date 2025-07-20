from products import Product


class Store:
    
    
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products


    def add_product(self, product):
        """adding a product to the store"""
        self.list_of_products.append(product)


    def remove_product(self, product):
        """remove product form the store"""
        for item in self.list_of_products:
            if item == product:
                self.list_of_products.remove(item)


    def get_total_quantity(self) -> int:
        """receive the quantity of everything"""
        quantity = 0
        for item in self.list_of_products:
            quantity += item.get_quantity()
        return quantity


    def get_all_products(self) -> list[Product]:
        """returns a list of active items"""
        active_items = []
        for item in self.list_of_products:
            if item.is_active():
                active_items.append(item)
        return active_items


    def order(self, shopping_list) -> float:
        """making the order"""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.buy(quantity) is None:
                return None
            else:
                total_price += product.buy(quantity)
        return total_price