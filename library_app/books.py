import file_handler
import crud
from os import path

PATH = path.join(path.dirname(__file__), "books.csv")

books = file_handler.read_file(PATH)


def get_keys():
    keys = list(books[0].keys())
    keys.remove("id")
    return keys


def list_books():
    # TODO: need better formatting for the output
    print(books)


def find_book():
    # TODO: error handling
    id = int(input("Add meg a keresendő könyv azonosítóját:"))
    print(crud.find_item(id, books))


def create_book():
    # v1
    # id = int(input("Add meg az új könyv azonosítóját:"))
    # title = input("Add meg az új könyv címét:")
    # author = input("Add meg az új könyv szerzőjét:")
    # new_book = {"id": id, "title": title, "author": author}
    # crud.create_item(new_book)
    # v2
    # keys = ["id", "title", "author"]
    # works only if the list is not empty
    keys = get_keys()
    book = {}
    for key in keys:
        value = input(f"Add meg az új könyv {key} mezőjét:")
        book.update({key: value})
    crud.create_item(book, books)
    file_handler.write_file(PATH, books)
    print("Könyv hozzáadva!")


def update_book():
    id = int(input("Add meg a módosítani kívánt könyv azonosítóját:"))
    book = crud.find_item(id, books)
    if book:
        keys = get_keys()
        for key in keys:
            data = input(
                f"Add meg az új {key} értéket, ha nem szeretnéd módosítani, nyomj entert!"
            )
            if data:
                book.update({key: data})
        crud.update_item(id, book, books)
        file_handler.write_file(PATH, books)
    else:
        print("Nincs ilyen könyv!")


def delete_book():
    id = int(input("Add meg a törölni kívánt könyv azonosítóját:"))
    crud.delete_item(id, books)
    file_handler.write_file(PATH, books)
    print("Könyv törölve!")
