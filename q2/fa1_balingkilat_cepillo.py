class Publication:
    title = ""
    author = ""
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return f"{self.__title}"

    def get_author(self):
        return f"{self.__author}"

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        get_title = self.get_title()
        get_author = self.get_author()
        print(f"Title: {get_title}")
        print(f"Author: {get_author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_of_pages}"

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("Number of pages must be positve")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return f"Issue Number: {self.__issue_number}"

    def set_issue_number(self, issue_number):
        if number_of_pages > 0:
            self.__issue_number = issue_number
        else:
            print("Number of pages must be positve")
        
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

