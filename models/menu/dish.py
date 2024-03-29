from models.menu.menu_item import MenuItem

class Dish(MenuItem):
    def __init__(self, name, price, desc):
        super().__init__(name, price)
        self.desc = desc

    def __str__(self):
        return self._name
    