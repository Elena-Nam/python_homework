import csv
import os 
import custom_module
from datetime import datetime

# Task 2
def read_employees():
    my_dict={}
    my_list=[]
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                my_dict['fields'] = headers
                my_list.append(row)
                my_dict['rows'] = my_list
    except Exception as e:
        print(f'An error occurred reading the file. {e}')        
    return(my_dict)

employees = read_employees()
print("Task 2: ", employees)

# Task 3
def column_index(str):
    column = employees["fields"].index(str)
    return(column)

employee_id_column = column_index("employee_id")

print("Task 3: ", column_index("first_name"))

# Task 4
def first_name(row_number):
    index = column_index("first_name")
    row = employees["rows"][row_number]
    print(row)
    return(row[index])
    
print("Task 4: ", employees)
print("Task 4: first name", first_name(2))

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

print("Task 5: ", employee_find(4))

# Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

print("Task 6: ", employee_find_2(4))
    
# Task 7
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[2])
    return employees["rows"]

print("Task 7: ", sort_by_last_name())

# Task 8
def employee_dict(row):
    return {employees["fields"][i]: row[i] for i in range(1,len(employees["fields"]))}
    
print("Task 8:", employee_dict(["rows"][0]))

# Task 9
def all_employees_dict():
    result_dict = {}
    for row in employees["rows"]:
        emp_id = row[0]
        result_dict[emp_id] = employee_dict(row)
    return result_dict

print("Task 9:", all_employees_dict())

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

print("Task 10:", get_this_value())

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("guess")

print("Task 11: ", custom_module.get_secret())

# Task 12
d1 = {}
d2 = {}
def read_minutes():
    try:
        with open('../csv/minutes1.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [tuple(row) for row in reader]
            d1["fields"] = headers
            d1["rows"] = rows
        with open('../csv/minutes2.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [tuple(row) for row in reader]
            d2["fields"] = headers
            d2["rows"] = rows
    except Exception as e:
        print(f'An error occurred reading the file. {e}')        
    return(d1, d2)

minutes1, minutes2 = read_minutes()

print("Task 12: ", (minutes1))

# Task 13
def create_minutes_set():
    set1 = set(d1["rows"])
    set2 = set(d2["rows"])
    union_set = set1.union(set2)
    return(union_set)
minutes_set = create_minutes_set()

print("Task 13:", minutes_set)

# Task 14
def create_minutes_list():
    resulting_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return (resulting_list)
minutes_list = create_minutes_list()

print("Task 14:", minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    new_list = tuple(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    
    try:
        with open('./minutes.csv', 'w', newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            for row in new_list:
                writer.writerow(row)
    except Exception as e:
        print(f'An error occurred reading the file. {e}')        
    
    return(new_list)

print("Task 15:", write_sorted_list())