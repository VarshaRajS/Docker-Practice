import mysql.connector

# Database configuration
db_config = {
    "host": "mysql_db",  # Matches the MySQL service name in docker-compose.yml
    "user": "root",
    "password": "password",
    "database": "bookstore_db"
}

def create_table():
    """Creates the books table if it doesn't already exist."""
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    );
    """)
    connection.close()
    print("Books table is ready.")

def add_book(title, author, price):
    """Adds a new book to the inventory."""
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, price) VALUES (%s, %s, %s)", (title, author, price))
    connection.commit()
    connection.close()
    print(f"Book '{title}' added successfully!")

def view_books():
    """Fetches and displays all books in the inventory."""
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books;")
    results = cursor.fetchall()
    connection.close()

    print("\nBooks in Inventory:")
    if results:
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Price: {row[3]}")
    else:
        print("No books found.")

def delete_book(book_id):
    """Deletes a book by ID."""
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    connection.commit()
    connection.close()
    print(f"Book with ID {book_id} deleted successfully!")

def main():
    create_table()
    while True:
        print("\nBookstore Inventory System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Delete Book by ID")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            add_book(title, author, price)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = int(input("Enter the book ID to delete: "))
            delete_book(book_id)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
