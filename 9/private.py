class Book:
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.__num_pages = None
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publisher = publisher

    @property
    def num_pages(self):
        return self.__num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        if num_pages > 0:
            self.__num_pages = num_pages
        else:
            raise ValueError("Number of pages must be greater than 0")


book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224, "0345391802", "Del Rey")
book.__num_pages = 224  # This will not work
print(book.num_pages)


class BouncyBall:
    def __init__(self):
        self.__price = None
        self.__size = None
        self.__brand = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be greater than 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 0:
            self.__size = size
        else:
            raise ValueError("Size must be greater than 0")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

