from models.rating import Rating

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._ratings = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category} | {self.active}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.calc_rating).ljust(25)} | {restaurant.active.ljust(25)}')

    """Returns a custom phrase based on _active property's value"""
    @property
    def active(self):
        return 'Active' if self._active else 'Inactive'
    
    """Alters the _active value between True and False"""
    def alter_state(self):
        self._active = not self._active

    """Adds a Rating object to the restaurant's rating list"""
    def add_rating(self, customer, grade):
        if 0 < grade < 5:
            rating = Rating(customer, grade)
            self._ratings.append(rating)

    """Calculates the average value of the ratings inside the array"""
    @property
    def calc_rating(self):
        if not self._ratings:
            return '-'
        
        ratings_sum = sum(rating._grade for rating in self._ratings)
        ratings_len = len(self._ratings)
        ratings_avg = round(ratings_sum / ratings_len, 1)
        return ratings_avg
