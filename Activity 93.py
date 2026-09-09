class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Confirmation: '{self.title}' has been successfully borrowed. ")

        else:
            print(f"Notice: '{self.title}' is already borrowed. ")

        def return_book(self):
            if self.is_borrowed:
                self.is_borrowed = False
                print(f"Confirmation: 'is already available in the library. ")
            else:
                print(f"Notice: '{self.title}'is already available in the library. ")

book1 = Book("The Hobbit", "J.R.R Tolkien")
book2 = Book("1984", "George Orwell")
book3 = Book("To kill a Mockingbird", "Harper Lee")

print("--- Borrowing Books ---")
book1.borrow()
book2.borrow()
book3.borrow()

print("\n--- Returning Books ---")
book1.return_book()
book2.return_book()
book3.return_book()