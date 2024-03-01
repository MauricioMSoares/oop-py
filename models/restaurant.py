class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category} | {self.active}'
    
    def list_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name} | {restaurant.category} | {restaurant.active}')

restaurant = Restaurant('Restaurant', 'Italian')
Restaurant.list_restaurants()