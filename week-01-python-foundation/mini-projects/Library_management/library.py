class Book():
    def __init__(self, name, book_type):
        self.name = name
        self.book_type = book_type
        self.is_available = True   #hardcoded-no need to pass as parameter

class Member():
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Library():
    def __init__(self):
        self.all_books = {}
        self.all_members = {}

    def add_book(self, name, book_type):
        new_book = Book(name, book_type)
        self.all_books[name] = new_book

    def search_book(self):
        book_to_search = input("Enter the book name to search :")
        if book_to_search in self.all_books:
            return self.all_books[book_to_search]  
        else:
            print("Book not found")   

    def register_member(self):
        member_name = input("Enter member name:")
        member_id = int(input("Enter the member id:"))
        new_member = Member(member_name,member_id)
        self.all_members[member_id] =  new_member 

    def borrow_book(self):
        name = input('Enter the name of the borrowing_book:')
        member = int(input("Enter the id of the member:"))
        date = input("Enter the return date:")
        if member in self.all_members:
            if name in self.all_books:
                if self.all_books[name].is_available == True:
                    print(f"The book {name} is borrowed by ID {member}.It is to be returned on or before{date}")
                    self.all_books[name].is_available = False
                else:
                    print("Cant borrow")
            else:
                print("Cant borrow")
        else:
            print("Borrowig book is not possible")            
    
    def return_book(self):
        name = input("Enter the book name:")
        is_on_time = input("Is the book returned on time(y/n):")
        if is_on_time  == "y":
            print("Returned on time .No fine")
        else:
            print("Returned Late. Py Fine")
        self.all_books[name].is_available = True


class Loan():
    def __init__(self,member, book_name, return_date):
        self.member = member
        self.book_name = book_name
        self.return_date = return_date

my_library = Library()

while True:
    print("Enter your choice:")
    print("1.Add Book")
    print("2.Register member")
    print("3.Search a Book")
    print("4.Borrow a Book")
    print("5.Return a Book")
    print("6.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        book_name = input("Enter the name of the book:")
        book_type = input("Enter the type of the book:")
        my_library.add_book(book_name, book_type)
    elif choice == "2":
        my_library.register_member()
    elif choice == "3":
        my_library.search_book()
    elif choice == "4":
        my_library.borrow_book()
    elif choice == "5":
        my_library.return_book()
    elif choice == "6":
        print("exiting..")
        break
    else:
        print("Enter a valid choice from 1-6")