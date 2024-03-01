from models.restaurant import Restaurant
from models.song import Song
from models.person import Person


def main():
    restaurant = Restaurant("Washoku no Ie", "Japanese")
    restaurant.alter_state()
    Restaurant.list_restaurants()

    song = Song("Sonata No. 14", "Beethoven", "15:00")
    Song.list_songs()

    person = Person("Naomi", "Project Manager", 25)
    print(person)
    person.birthday()
    print(person)
    print(person.salutation)

if __name__ == "__main__":
    main()
