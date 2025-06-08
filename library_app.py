from entities.items.book import Book
from entities.items.dvd import Dvd, Genre
from entities.library import Library
from entities.items.magazine import Magazine
from entities.member import Member
import itertools

def get_genre_from_input(genre_input: str) -> Genre:
    for genre in Genre:
        if genre.value.lower() == genre_input.strip().lower():
            return genre
    raise ValueError(f"Nieznany gatunek: {genre_input}")

def add_item() -> None:
    print("\n Jaką pozycję chcesz dodać?")
    print("1. Dodaj książkę")
    print("2. Dodaj magazyn")
    print("3. Dodaj DVD")
    user_input_item = input("Podaj opcję: ")
    if user_input_item == "1":
        add_book()
    elif user_input_item == "2":
        add_magazine()
    elif user_input_item == "3":
        add_dvd()
    else:
        raise ValueError("Niepoprawna wartość")

def add_book() -> None:
    print("\n Tworzysz książkę.")
    title = input("Podaj tytuł: ")
    author = input("Podaj autora: ")
    year = int(input("Podaj rok: "))

    id = next(id_iter)
    user_library.add_item(
        Book(
            id=id,
            title=title,
            year=year,
            author=author
        )
    )

    print(f"Pomyślnie dodano książkę:")
    print(f"ID: {id}")
    print(f"Tytuł: '{title}'")
    print(f"Autor: '{author}'")
    print(f"Rok wydania: {year}")

def add_magazine() -> None:
    print("\n Tworzysz magazyn.")
    title = input("Podaj tytuł: ")
    editor = input("Podaj edytora magazynu: ")
    year = int(input("Podaj rok: "))

    id = next(id_iter)
    user_library.add_item(
        Magazine(
            id=id,
            title=title,
            year=year,
            editor=editor
        )
    )

    print(f"Pomyślnie dodano magazyn:")
    print(f"ID: {id}")
    print(f"Tytuł: '{title}'")
    print(f"Edytor: '{editor}'")
    print(f"Rok wydania: {year}")

def add_dvd() -> None:
    print("\n Tworzysz DVD.")
    title = input("Podaj tytuł: ")
    director = input("Podaj reżysera filmu: ")
    year = int(input("Podaj rok: "))
    length = int(input("Podaj długość filmu w minutach: "))
    genre = input("Podaj gatunek. Gatunki do wyboru"
                  "\nAction"
                  "\nComedy"
                  "\nThriller"
                  "\nHorror"
                  "\nScience Fiction"
                  "\nDocumentary"
                  "\nRomance"
                  "\nAnimation\n")

    genre = get_genre_from_input(genre)

    id = next(id_iter)
    dvd = Dvd(
        id=id,
        title=title,
        year=year,
        director=director,
        length_in_minutes=length,
        genre=genre
    )

    user_library.add_item(dvd)

    print(f"Pomyślnie dodano DVD: "
          f"\nID: {id}"
          f"\nTytuł: '{title}'"
          f"\nReżyser: '{director}'"
          f"\nRok wydania: {year}",
          f"\n{dvd.show_movie_length()}",
          f"\nGatunek: {genre.value}"
          )

def add_member() -> None:
    print("\nDodajesz członka.")
    name = input("Podaj imię: ")
    lastname = input("Podaj nazwisko: ")
    email = input("Podaj email: ")

    member = Member(
        member_id=next(id_iter),
        name=name,
        last_name=lastname,
        email=email,
        rented_items=[]
    )

    user_library.add_member(member)

    print(f"Pomyślnie dodano członka:")
    print(f"ID: {member.member_id}")
    print(f"Imię: '{name}'")
    print(f"Nazwisko: '{lastname}'")
    print(f"Email: {email}")

def borrow_item() -> None:
    print("\nJaki członek wypożycza książkę? Podaj ID")
    for member in user_library.members:
        print(f"ID: {member.member_id}, {member.name} {member.last_name}")

    user_input_member_id = int(input("Podaj ID członka: "))

    print("\nJaką pozycję chcesz wypożyczyć? Podaj ID")
    for item in user_library.get_all_available_items():
        print(f"ID: {item.id}, Tytuł: '{item.title}'")

    user_input_item_id = int(input("Podaj ID pozycji: "))

    item = next((item for item in user_library.items if item.id == user_input_item_id), None)
    member = next((member for member in user_library.members if member.member_id == user_input_member_id), None)

    user_library.add_rental(item, member)

    print(f"{member.name} {member.last_name} wypożyczył {item.title}")
    print(f"Data wypożyczenia: {user_library.rentals[-1].rent_date}")
    print(f"Data oddania: {user_library.rentals[-1].return_date}")

def return_book() -> None:
    print("\nJaki członek oddaje książkę? Podaj ID")
    for member in user_library.members:
        print(f"ID: {member.member_id}, {member.name} {member.last_name}")

    user_input_member_id = int(input("Podaj ID członka: "))

    print("\nJaką pozycję chcesz zwrócić? Podaj ID")
    for item in user_library.get_all_rented_items():
        print(f"ID: {item.id}, Tytuł: '{item.title}'")

    user_input_item_id = int(input("Podaj ID pozycji: "))

    member = next((member for member in user_library.members if member.member_id == user_input_member_id), None)
    item_to_return = next((item for item in user_library.items if item.id == user_input_item_id), None)

    found = False

    for rental in member.rented_items:
        if rental.item == item_to_return:
            user_library.remove_rental(rental, member)
            print(f"{member.name} {member.last_name} zwrócił {item_to_return.title}")
            if rental.is_overdue():
                print(
                    f"{member.name} {member.last_name} ma do zapłacenia karę w wysokości {rental.item.calculate_overdue_charge()}")
            found = True
            break

    if not found:
        print("Członek nie wypożyczył tej pozycji.")


if __name__ == "__main__":
    id_iter = itertools.count()

    while True:
        user_library = Library()

        print("\n System wypożyczalni mediów w bibliotece")
        print("1. Dodaj pozycję")
        print("2. Dodaj członka")
        print("3. Wypożycz książkę")
        print("4. Zwróć książkę")
        print("5. Pokaż wszystkich członków, którzy spóźniają się z zwrotem")
        print("6. Pokaż wszystkie dostępne pozycje")
        print("7. Ustaw dzienną karę za nieoddanie książki")
        print("8. Wyświetl wszystkie wypożyczenia")

        user_input = input("Podaj opcję: ")

        if user_input == "1":
            add_item()

        elif user_input == "2":
            add_member()

        elif user_input == "3":
            borrow_item()

        elif user_input == "4":
            return_book()

        elif user_input == "5":
            members = user_library.get_all_members_with_overdue()
            for member in members:
                print(f"ID: {member.member_id}, {member.name} {member.last_name}")

        elif user_input == "6":
            items = user_library.get_all_available_items()
            for item in items:
                print(f"ID: {item.id}, tytuł: {item.title}")

        elif user_input == "7":
            fine = float(input("Podaj karę dzienną za nieoddanie książki: "))
            user_library.daily_fine_for_overdue_items = fine
            print(f"Ustawiono karę na {user_library.daily_fine_for_overdue_items}")

        elif user_input == "8":
            for rental in user_library.rentals:
                print(f"Wypożyczony przedmiot: {rental.item.title} | Data wypożyczenia: {rental.rent_date} | Data Oddania: {rental.return_date} | Wypożyczone przez: {rental.member.name} {rental.member.last_name}")

        else:
            raise ValueError("Niepoprawna wartość")

