import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# Create a DataFrame from a dictionary:

my_dict  = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(my_dict)
print(task1_data_frame)

# Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print ("\n", task1_with_salary)

# Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print("\n", task1_older)

# Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index = False)


# Task 2: Loading Data from CSV and JSON
# Read data from a CSV file:
task2_employees = pd.read_csv("employees.csv")
print("\n", 'Task 2:' , task2_employees)

# Read data from a JSON file:

json_employees = pd.read_json("additional_employees.json")
print("\n", json_employees)

# Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\n", more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# Use the head() method:
first_three = more_employees.head(3)
print("\n", first_three)

# Use the tail() method:
last_two = more_employees.tail(2)
print("\n", last_two)

# Get the shape of a DataFrame
employee_shape = more_employees.shape
print("\n", employee_shape)

# Use the info() method:
print("\n", more_employees.info())


# Task 4: Data Cleaning
# Task 4.1 
dirty_data = pd.read_csv("dirty_data.csv")
print("\n", dirty_data)

clean_data = dirty_data.copy()

# Task 4.2
clean_data = clean_data.drop_duplicates()
print("\n", clean_data)

# Task 4.3
clean_data["Age"] = clean_data["Age"].replace("unknown", pd.NA)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\n", "Task 4.3: ", clean_data)

# Task 4.4
clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\n", "Task 4.4: ", clean_data)

# Task 4.5
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
print("\n", "Task 4.5: Average age ", clean_data)

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("\n", "Task 4.5: Median salary ", clean_data)

# Task 4.6
clean_data["Hire Date"] = pd.to_datetime (clean_data["Hire Date"], errors = "coerce")
print("\n", "Task 4.6: ", clean_data)

# Task 4.7
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
print("\n", "Task 4.7:", clean_data)