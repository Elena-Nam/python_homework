import sqlite3

with sqlite3.connect("company.db") as conn:
    cursor = conn.cursor()

    # Create Departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
  # Drop existing Employees table to update its schema
    # cursor.execute("DROP TABLE IF EXISTS Employees")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INTEGER,
            salary REAL,
            FOREIGN KEY (department_id) REFERENCES Departments(id)
        );
    """)
  

    # Create Projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        );
    """)

    # Insert departments
    departments = [
        (10, 'HR'),
        (20, 'IT'),
        (30, 'Finance')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Departments (id, name) VALUES (?, ?)", departments)

    # Insert employees
    employees = [
        (101, 'Alice', 10, 90000),
        (102, 'Bob', 10, 90000),
        (201, 'Charlie', 20, 85000),
        (202, 'David', 20, 80000),
        (301, 'Eva', 30, 95000)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO Employees (employee_id, name, department_id, salary)
        VALUES (?, ?, ?, ?)
    """, employees)

    # Insert projects
    projects = [
        ('Project A', 'HR'),
        ('Project B', 'IT'),
        ('Project C', 'Finance')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Projects (name, department) VALUES (?, ?)", projects)

    # Query: Employees working on 'Project A'
    # query = """
    #     SELECT e.name, p.name AS project_name
    #     FROM Employees e
    #     JOIN Departments d ON e.department_id = d.id
    #     JOIN Projects p ON d.name = p.department
    #     WHERE p.name = 'Project B';
    # """
    # cursor.execute(query)
    # results = cursor.fetchall()

    # for row in results:
    #     print(row)

# 8.3   
with sqlite3.connect("company.db") as conn:
    cursor = conn.cursor()
    # cursor.execute ("""
    #     SELECT department_id, 
    #         MIN(salary) AS min_salary, 
    #         MAX(salary) AS max_salary, 
    #         COUNT(employee_id) AS num_employees
    #     FROM Employees
    #     GROUP BY department_id;
    # """)
    # results = cursor.fetchall()
    # print("Task 8.3:")
    # for row in results:
    #     print(row)
    cursor.execute ("""
        SELECT d.name AS department_name,
            e.department_id,
            MIN(e.salary) AS min_salary,
            MAX(e.salary) AS max_salary,
            COUNT(e.employee_id) AS num_employees
        FROM Employees e
        JOIN Departments d ON e.department_id = d.id
        GROUP BY e.department_id, d.name;
        """)
    results = cursor.fetchall()
    print("Task 8.3:")
    for row in results:
        print(row)
   