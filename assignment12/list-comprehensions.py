import pandas as pd

# Task 3

df= pd.read_csv("../csv/employees.csv")
# list of full names
employee_list = [row['first_name'] + ' ' + row['last_name'] for index, row in df.iterrows()]
print("All Employees:", employee_list)

# Filter names that contain the letter "e"
names_with_e = [name for name in employee_list if 'e' in name.lower()]
print("Names with 'e':", names_with_e)