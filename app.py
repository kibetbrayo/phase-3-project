import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Book, Review, Base

# Create an SQLite database and tables
engine = create_engine('sqlite:///books_library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def print_menu():
    print("Welcome to the Books Library")
    print("Menu:")
    print("1. Browse Books")
    print("2. View Book Details")
    print("3. Add a Book")
    print("4. Delete a Book")
    print("5. List All Books")
    print("6. Add a Review")
    print("q. Quit")
    print()

@click.group()
def cli():
    pass

@cli.command()
def browse_books():
    """Browse Books in the library"""
    print_menu()
    books = session.query(Book).all()

    if books:
        print("Available Books:")
        for book in books:
            print(f"Book ID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Book Code: {book.book_code}")
            print("--------------------")
    else:
        print("No books available.")

@cli.command()
def view_book_details():
    """View Book Details"""
    print_menu()
    book_id = int(input("Enter the book ID: "))
    book = session.query(Book).filter_by(id=book_id).first()

    if book:
        print("Book Details:")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Book Code: {book.book_code}")
    else:
        print("Book not found.")

@cli.command()
def add_book():
    """Add a Book Title"""
    print_menu()
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    book_code = input("Enter the book_code of the book: ")

    new_book = Book(title=title, author=author, book_code=book_code)
    session.add(new_book)
    session.commit()

    print("Book added successfully.")

@cli.command()
def delete_book():
    """Delete Book in the library"""
    print_menu()
    book_id = int(input("Enter the book ID to delete: "))
    book = session.query(Book).filter_by(id=book_id).first()

    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully.")
    else:
        print("Book not found.")

@cli.command()
def list_all_books():
    """List All Books"""
    print_menu()
    print("List of All Books:")
    books = session.query(Book).all()

    if books:
        for book in books:
            print(f"Book ID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Book Code: {book.book_code}")
            print("--------------------")
    else:
        print("No books available.")

@cli.command()
def add_review():
    """Add a Review"""
    print_menu()
    book_id = int(input("Enter the book ID for the review: "))
    rating = int(input("Enter your rating for the book (1-5): "))
    comment = input("Enter your review comment: ")

    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print("Book not found.")
        return

    new_review = Review(rating=rating, comment=comment, user_id=1, book_id=book_id)
    session.add(new_review)
    session.commit()

    print("Review added successfully.")

if __name__ == '__main__':
    try:
        while True:
            print_menu()
            choice = input("Enter the number of the command you want to run (or 'q' to quit): ")
            
            if choice == '1':
                browse_books()
            elif choice == '2':
                view_book_details()
            elif choice == '3':
                add_book()
            elif choice == '4':
                delete_book()
            elif choice == '5':
                list_all_books()
            elif choice == '6':
                add_review()
            elif choice == 'q':
                break
            else:
                print("Invalid choice. Please select a valid command or 'q' to quit.")
    finally:
        print("Thank you for using Books Library")
