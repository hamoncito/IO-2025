# System wypożyczalni mediów w bibliotece

Projekt przedstawia system służący do obsługi wypożyczeń mediów w bibliotece. Umożliwia on zarządzanie zasobami (książkami, magazynami, płytami DVD), monitorowanie aktywności członków oraz śledzenie historii i zaległości w zwrotach. System pozwala również na naliczanie kar za przetrzymane wypożyczenia.

## Cel projektu

Projekt powstał w ramach zajęć z Inżynierii Oprogramowania. Celem było stworzenie w pełni funkcjonalnego, dobrze udokumentowanego i przetestowanego systemu zarządzania biblioteką z wykorzystaniem języka Python i narzędzi zespołowych GitHub.

## Wymagania projektowe

- Implementacja modelu dziedzinowego w Pythonie obejmującego co najmniej 5 klas z odpowiednimi typami danych i metodami.
- Umieszczenie każdej klasy w osobnym pliku z kompletnym docstringiem opisującym jej funkcjonalność.
- Przygotowanie co najmniej 15 testów jednostkowych oraz 3 testów integracyjnych.
- Zastosowanie workflow GitHub:
  - rozwój funkcjonalności na osobnych branchach,
  - pull requesty z komentarzami i review,
  - akceptacja (approve) zmian.
- Przygotowanie pliku README w formacie Markdown opisującego założenia, strukturę i zastosowania systemu.

## Architektura klas i struktura projektu

### Klasy

- `Item` – klasa abstrakcyjna definiująca wspólne cechy pozycji wypożyczalni (tytuł, autor, dostępność).
- `Book`, `Magazine`, `DVD` – klasy dziedziczące po `Item`, reprezentujące konkretne typy pozycji.
- `Rental` – klasa opisująca proces wypożyczenia i zwrotu pozycji, uwzględniająca daty i opóźnienia.
- `Member` – klasa reprezentująca członka biblioteki; przechowuje dane osobowe i listę wypożyczeń.
- `Library` – główna klasa koordynująca wypożyczenia, pozycje i członków; zarządza karami i dostępnością.

## Zespół projektowy

| Imię i nazwisko       | GitHub          | Zakres prac                                                               |
|------------------------|------------------|---------------------------------------------------------------------------|
| Agnieszka Popiel       | `@hamoncito`     | Diagram UML, koordynacja zespołu, klasy `Item`, `Book`, testy `Book`     |
| Piotr Wilma            | `@Wilsonuep`     | README, klasy `Library`, `Member`                                        |
| Aleksandra Panek       | `@ompanek`       | Klasy `DVD`, `Magazine`, testy jednostkowe                               |
| Piotr Cerk             | `@1nterring`     | Klasa `Rental`, testy jednostkowe `Rental`                               |
| Wiktoria Pawlak        | `@wikipw`        | Testy jednostkowe `Library`, `Member`, testy integracyjne                |

## Wymagane biblioteki

Projekt opiera się na standardowej bibliotece Pythona. Wykorzystywane moduły to:

- `abc`
- `typing`
- `datetime`
- `itertools`
- `__future__`
- `unittest`
- `enum`

## Scenariusze użycia

### Scenariusz 1: Codzienne zarządzanie wypożyczeniami
Pracownik biblioteki rejestruje nowych członków, dodaje nowe książki oraz wypożycza pozycje użytkownikom. Dzięki klasie `Library`, cały proces przebiega z zachowaniem kontroli dostępności pozycji oraz powiązania ich z członkami.

### Scenariusz 2: Monitorowanie zaległości i naliczanie kar
Na koniec dnia bibliotekarz wywołuje metodę `get_overdue_rentals`, aby uzyskać listę wypożyczeń po terminie. Na podstawie długości opóźnienia i ustawionej stawki dziennej system nalicza odpowiednie kary i informuje użytkownika podczas zwrotu.

### Scenariusz 3: Kontrola użytkowników
Bibliotekarz analizuje aktywność członka: jakie pozycje są obecnie przez niego wypożyczone, czy posiada zaległości. Klasa `Member` pozwala wygodnie zarządzać wypożyczeniami danego użytkownika i śledzić przekroczenia terminów.

### Scenariusz 4: Generowanie raportu stanu zasobów
System może w każdej chwili zwrócić listę wszystkich dostępnych pozycji (`get_all_available_items`) oraz historii wszystkich wypożyczeń (`get_all_rentals`). Dane te mogą zostać użyte do tworzenia miesięcznych raportów bibliotecznych.

## Licencja
Projekt edukacyjny. Do użytku dydaktycznego oraz jako baza do rozbudowy i dalszego rozwoju.