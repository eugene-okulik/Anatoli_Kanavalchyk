class Book:
    pages_material = 'paper'
    presented_text = True

    def __init__(self, book_name, author, pages_quantity, pages_isbn, reserved=False):
        self.book_name = book_name
        self.author = author
        self.pages_quantity = pages_quantity
        self.pages_isbn = pages_isbn
        self.reserved = reserved

    def __str__(self):
        book_details = (
            f"Название: {self.book_name}, Автор: {self.author}, "
            f"Страниц: {self.pages_quantity}, Материал: {self.pages_material}"
        )
        if self.reserved:
            book_details += ", зарезервирована"
        return book_details


books = [
    Book("Идиот", "Достоевский", 500, "978-5-17-078118-4"),
    Book("Преступление и наказание", "Достоевский", 430, "978-5-17-066853-8"),
    Book("Война и мир", "Толстой", 1225, "978-5-17-068858-1"),
    Book("Анна Каренина", "Толстой", 864, "978-5-17-069517-6"),
    Book("Мастер и Маргарита", "Булгаков", 480, "978-5-17-070141-9", reserved=True)
]

books[1].reserved = True

for book in books:
    print(book)


class Textbook(Book):
    def __init__(self, book_name, author, pages_quantity, pages_isbn, subject, grade, has_assignments, reserved=False):
        super().__init__(book_name, author, pages_quantity, pages_isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_assignments = has_assignments

    def __str__(self):
        details = (
            f"Название: {self.book_name}, Автор: {self.author}, "
            f"Страниц: {self.pages_quantity}, Предмет: {self.subject}, Класс: {self.grade}"
        )
        if self.reserved:
            details += ", зарезервирована"
        return details


textbooks = [
    Textbook("Алгебра", "Иванов", 200, "978-5-17-089652-0", "Математика", 9, True),
    Textbook("География", "Петров", 150, "978-5-17-089653-7", "География", 8, True),
    Textbook("История", "Сидоров", 180, "978-5-17-089654-4", "История", 10, False),
    Textbook("Физика", "Кузнецов", 220, "978-5-17-089655-1", "Физика", 11, True),
    Textbook("Биология", "Смирнова", 190, "978-5-17-089656-8", "Биология", 7, False, reserved=True)
]

textbooks[0].reserved = True

for textbook in textbooks:
    print(textbook)
