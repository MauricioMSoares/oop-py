from models.restaurant import Restaurant
from models.song import Song
from models.person import Person
from models.book import Book

def main():
    restaurant = Restaurant("Washoku no Ie", "Japanese")
    restaurant.alter_state()
    restaurant.add_rating('Leah', 5)
    Restaurant.list_restaurants()

    Song("Sonata No. 14", "Beethoven", "15:00")
    Song.list_songs()

    person = Person("Naomi", "Project Manager", 25)
    print(person)
    person.birthday()
    print(person)
    print(person.salutation)

    book = Book('Tabibito no Ryokou', 'Naomi Kawazaki', 2004)
    print(book)
    print(Book.check_availability(2004))
    book.lend()
    print(book)

if __name__ == "__main__":
    main()
