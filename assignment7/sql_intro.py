import sqlite3

def add_publisher(cursor, publisher_name):
    try:
        cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)", (publisher_name,))
    except sqlite3.IntegrityError:
        print(f"{publisher_name} is already in the database.")

def add_magazine(cursor, magazine_name, publisher_name):
    cursor.execute("SELECT publisher_id FROM Publishers WHERE publisher_name = ?", (publisher_name,))
    publisher_ids = cursor.fetchall()
    if publisher_ids:
        publisher_id = publisher_ids[0][0]
        try:
            cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?, ?)", (magazine_name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"{magazine_name} is already in the database.")
    else:
        print(f"Publisher {publisher_name} not found.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM Subscribers WHERE subscriber_name = ? AND sub_address = ?", (name, address))
    if not cursor.fetchall():
        try:
            cursor.execute("INSERT INTO Subscribers (subscriber_name, sub_address) VALUES (?, ?)", (name, address))
        except sqlite3.IntegrityError:
            print(f"{name} at {address} is already in the database.")

def add_subscription(cursor, subscriber_name, magazine_name):
    cursor.execute("SELECT subscriber_id FROM Subscribers WHERE subscriber_name = ?", (subscriber_name,))
    sub_ids = cursor.fetchall()
    cursor.execute("SELECT magazine_id FROM Magazines WHERE magazine_name = ?", (magazine_name,))
    mag_ids = cursor.fetchall()
    
    if sub_ids and mag_ids:
        subscriber_id = sub_ids[0][0]
        magazine_id = mag_ids[0][0]
        cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        if not cursor.fetchall():
            try:
                cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id) VALUES (?, ?)", (subscriber_id, magazine_id))
            except sqlite3.IntegrityError:
                print(f"Subscription already exists.")
    else:
        print("Subscriber or magazine not found.")

with sqlite3.connect("./db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()

    # Drop old tables (optional during development)
    cursor.execute("DROP TABLE IF EXISTS Subscriptions")
    cursor.execute("DROP TABLE IF EXISTS Subscribers")
    cursor.execute("DROP TABLE IF EXISTS Magazines")
    cursor.execute("DROP TABLE IF EXISTS Publishers")
    try:
    # Recreate all tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Publishers (
                publisher_id INTEGER PRIMARY KEY,
                publisher_name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Magazines (
                magazine_id INTEGER PRIMARY KEY,
                magazine_name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER,
                FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                subscriber_name TEXT NOT NULL,
                sub_address TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                magazine_id INTEGER,
                subscriber_id INTEGER,
                FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
                FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
                UNIQUE (magazine_id, subscriber_id)
            )
        """)    
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

    # Insert data into all tables
    add_publisher(cursor, 'Oxford University')
    add_publisher(cursor, 'Cambridge Press')
    add_publisher(cursor, 'Harvard Publishing')

    add_magazine(cursor, 'Solution', 'Oxford University')
    add_magazine(cursor, 'Science Weekly', 'Cambridge Press')
    add_magazine(cursor, 'Thinkers Digest', 'Harvard Publishing')

    add_subscriber(cursor, 'Elena', 'Far Far Away')
    add_subscriber(cursor, 'Tom', '123 Apple Lane')
    add_subscriber(cursor, 'Jane', '456 Banana St')

    add_subscription(cursor, 'Elena', 'Solution')
    add_subscription(cursor, 'Tom', 'Science Weekly')
    add_subscription(cursor, 'Jane', 'Thinkers Digest')

    conn.commit()
    print("Tables created and sample data inserted successfully.")


# Write a query to retrieve all information from the subscribers table
try:
    cursor.execute('SELECT * From Subscribers')
    subscribers = cursor.fetchall()
    for subscriber in subscribers:
        print(subscriber)
except sqlite3.Error as e:
    print(f"Error retrieving subscribers: {e}")  

# Write a query to retrieve all magazines sorted by name.
try:
    cursor.execute('SELECT * From Magazines ORDER BY magazine_name')
    magazines = cursor.fetchall()
    print("\n")
    for magazine in magazines:
        print(magazine)
except sqlite3.Error as e:
            print(f"Error retrieving magazines: {e}")


# Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
try:  
    cursor.execute("""
        SELECT Magazines.magazine_name
        FROM Magazines
        JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id
        WHERE Publishers.publisher_name = 'Oxford University';
    """)
    results = cursor.fetchall()
    print("\n")
    for row in results:
        print(row)
except sqlite3.Error as e:
            print(f"Error retrieving magazines for publisher: {e}")


