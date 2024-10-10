def read_file(file_path):
    # TODO: use csv module in real life
    with open(file_path, "r", encoding="UTF-8") as file:
        books = []
        for line in file:
            id, title, author = line.rstrip().split(";")
            books.append(
                {
                    "id": int(id),
                    "title": title,
                    "author": author,
                }
            )
    return books


def write_file(file_path, books):
    with open(file_path, "w", encoding="UTF-8") as file:
        for book in books:
            # TODO: remove the first line break, and create one string, call wrtie only once
            # use restrip or slicing to remove it
            book_line = "\n" + ";".join(str(value) for value in book.values())
            file.write(book_line)
