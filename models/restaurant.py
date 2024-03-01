class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category} | {self.active}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | Status'.ljust(25))
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active.ljust(25)}')

    @property
    def active(self):
        return 'Active' if self._active else 'Inactive'
    
    def alter_state(self):
        self._active = not self._active
