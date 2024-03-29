from models.menu.menu_item import MenuItem

class Dish(MenuItem):
    def __init__(self, name, price, desc):
        super().__init__(name, price)
        self.desc = desc

    def __str__(self):
        return self._name
    
    def apply_discount(self):
        self._price -= (self._price * 0.08)
    