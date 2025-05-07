import sqlite3

# Task 1
with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()
    cursor.execute ("""
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o 
    JOIN line_items li ON o.order_id = li.order_id 
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id 
    LIMIT 5;
    """)
    print("Tables joined successfully.")
    results = cursor.fetchall()
    print("Task 1: ")
    for order_id, total_price in results:
        print(f"Order ID: {order_id}, Total Price: {total_price:.2f}")
  
# Task 2

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) sub ON c.customer_id = sub.customer_id_b
    GROUP BY c.customer_id;
    """)
    
    print("Task 2:")
    results = cursor.fetchall()
    for customer_name, average_total_price in results:
        avg_str = f"{average_total_price:.2f}" if average_total_price is not None else "No orders"
        print(f"Customer: {customer_name}, Average Order Total: {avg_str}")


# Task 3

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()

    # 1: Get customer_id for 'Perez and Sons'
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
    customer_row = cursor.fetchone()
    customer_id = customer_row[0]

    #  2: Get employee_id for 'Miranda Harris'
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_row = cursor.fetchone()
    employee_id = employee_row[0]

    #  3: Get 5 least expensive product_ids
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    product_rows = cursor.fetchall()
    if len(product_rows) < 5:
        raise ValueError("Less than 5 products found.")
    product_ids = [row[0] for row in product_rows]

    #  4: Begin transaction
    conn.execute("BEGIN")

    try:
        #  5: Insert order and retrieve its order_id using RETURNING
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        #  6: Insert 5 line_items using the returned order_id
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, product_id, 10))  # 10 of each product

        #  7: Commit transaction
        conn.commit()
        print("Task 3: ")
        print(" Order and line items inserted successfully.")

    except Exception as e:
        conn.rollback()
        print(" Transaction failed. Rolled back.")
        raise e

    #  8: Display inserted line_items
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
    """, (order_id,))

    results = cursor.fetchall()
    print("\n Line items for the new order:")
    for line_item_id, quantity, product_name in results:
        print(f"Line Item ID: {line_item_id}, Quantity: {quantity}, Product: {product_name}")

# the same code for sql shell 
# PRAGMA foreign_keys = ON;

# SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';
# SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';
# SELECT product_id FROM products ORDER BY price ASC LIMIT 5;

# BEGIN;

# INSERT INTO orders (customer_id, employee_id, date)
# VALUES (3, 2, DATE('now'))
# RETURNING order_id;

# INSERT INTO line_items (order_id, product_id, quantity) VALUES (22, 4, 10);
# INSERT INTO line_items (order_id, product_id, quantity) VALUES (22, 5, 10);
# INSERT INTO line_items (order_id, product_id, quantity) VALUES (22, 6, 10);
# INSERT INTO line_items (order_id, product_id, quantity) VALUES (22, 7, 10);
# INSERT INTO line_items (order_id, product_id, quantity) VALUES (22, 8, 10);

# COMMIT;

# SELECT li.line_item_id, li.quantity, p.product_name
# FROM line_items li
# JOIN products p ON li.product_id = p.product_id
# WHERE li.order_id = 22;

# Task: Use sqlcommand to delete the line_items records for the order you created. (This is one delete statement.) Delete also the order record you created.
# 1: Delete line_items for the order created (using order_id)
# DELETE FROM line_items 
# WHERE order_id = (SELECT MAX(order_id) FROM orders);

# 2: Delete the order record (using order_id)
# DELETE FROM orders 
# WHERE order_id = (SELECT MAX(order_id) FROM orders);


# Task 4

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name
        HAVING COUNT(o.order_id) > 5;
        """)
    results = cursor.fetchall()
    print("Task 4: ")
    print(results)