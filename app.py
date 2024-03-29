from models.restaurant import Restaurant
from models.song import Song
from models.person import Person
from models.book import Book
from models.menu.menu_item import MenuItem
from models.menu.dish import Dish
from models.menu.drink import Drink
from models.menu.dessert import Dessert

import requests
import json


def main():
    api_call()


def api_call():
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = response.json()
        restaurant_data = {}
        for item in data:
            name = item["Company"]
            if name not in restaurant_data:
                restaurant_data[name] = []

            restaurant_data[name].append(
                {
                    "item": item["Item"],
                    "price": item["price"],
                    "desc": item["description"],
                }
            )

    else:
        print(f"Error: {response.status_code}")

    for name, data in restaurant_data.items():
        file_name = f"{name}.json"
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)



def menu_test():
    restaurant = Restaurant("Washoku no Ie", "Japanese")
    drink = Drink("Orange Juice", 4.90, "Large")
    dish = Dish("Croissant", 6.90, "The original flavour of France")
    dessert = Dessert("Brigadeiro", 2.90, "Brazilian Confectionery", "Medium")

    drink.apply_discount()
    dish.apply_discount()
    dessert.apply_discount()

    restaurant.add_at_menu(drink)
    restaurant.add_at_menu(dish)
    restaurant.add_at_menu(dessert)
    restaurant.show_menu


def test():
    restaurant = Restaurant("Washoku no Ie", "Japanese")
    restaurant.alter_state()
    restaurant.add_rating("Leah", 5)
    Restaurant.list_restaurants()

    Song("Sonata No. 14", "Beethoven", "15:00")
    Song.list_songs()

    person = Person("Naomi", "Project Manager", 25)
    print(person)
    person.birthday()
    print(person)
    print(person.salutation)

    book = Book("Tabibito no Ryokou", "Naomi Kawazaki", 2004)
    print(book)
    print(Book.check_availability(2004))
    book.lend()
    print(book)


if __name__ == "__main__":
    main()
