from models.menu.menu_item import MenuItem

class Dessert(MenuItem):
    def __init__(self, name, price, type, size):
        super().__init__(name, price)
        self.type = type
        self.size = size
    
    def __str__(self):
        return self._name
    
    def apply_discount(self):
        self._price -= (self._price * 0.03)
