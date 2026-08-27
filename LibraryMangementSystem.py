#LIBRARY MANAGEMENT SYSTEM
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


class Member(Book):
    def __init__(self, title, author, member_name):
        super().__init__(title, author)
        self.member_name = member_name

    def show_member(self):
        self.show_book()
        print("Member Name:", self.member_name)


m1 = Member("The Great Gatsby", "F. Scott Fitzgerald", "Youraj\n")
m2 = Member("The Catcher in the Rye", "J.D. Salinger", "Raunak\n")
m3 = Member("Pride and Prejudice", "Jane Austen", "Raghuraj")

m1.show_member()
m2.show_member()
m3.show_member()