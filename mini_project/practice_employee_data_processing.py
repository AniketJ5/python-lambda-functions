import csv

# Read Employee Records
## Extract

employees = []

with open('employees.csv','r',newline='') as file:
    reader = csv.DictReader(file)
    print(reader)

    for row in reader:
        row['salary'] = int(row['salary'])
        row['employee_id'] = int(row['employee_id'])
        employees.append(row)

# print("\nOriginal Employee Records\n")

# for emp in employees:
#     print(emp)


# Transform Employee Names (upper)
## Transform
transformed = list(map(lambda e: {**e, "name": e["name"].upper()},employees))

# print(transformed)
# Filter Employees by Departments (IT)
## filter() function
it_employees = list(filter(lambda e:e["department"] == "IT",transformed))
# print(it_employees)

# Filter Active Employees
active_employees = list(filter(lambda e:e["status"] == "Active",it_employees))
# print(active_employees)

# Sort by Salary
sorted_salary = list(sorted(active_employees,key=lambda e:e['salary'],reverse=True))
# print(sorted_salary)

# Calculate Bonus (10%)
calculated_bonus = list(map(lambda e: {**e,"bonus" : round(e["salary"]*0.10,3)},sorted_salary))
# print(calculated_bonus)

# Summary Statistics
total_salary = sum(map(lambda e: e["salary"],calculated_bonus))
print(total_salary)

average_salary = (total_salary/len(calculated_bonus))
print(average_salary)

highest_salary = max(calculated_bonus,key=lambda e:e['salary'])
print(highest_salary)

lowest_salary = min(calculated_bonus,key=lambda e:e['salary'])
print(lowest_salary)

# Print Report
print("\nProcessed Employees\n")

for emp in calculated_bonus:
    print(emp)

print("\nSummary Report\n")
print("="*30)
print("Total Employees  : ", len(calculated_bonus))
print("Total Salary     : ", total_salary)
print("Average Salary   : ", average_salary)
print("Highest Salary   : ", highest_salary)
print("Lowest Salary    : ", lowest_salary)
print("="*30)

# Export Processed Data
## loading
with open('processed_employees.csv',"w",newline='') as file:

    Fields = ["employee_id","name","department","salary","status","bonus"]

    writer = csv.DictWriter(file,fieldnames=Fields)

    writer.writeheader()
    writer.writerows(calculated_bonus)

print("\nProcessed Data Exported Succesfully\n")

# Export Summary Report
## Loading
with open('summary_report.txt',"w") as file:

    file.write("Employees Summary Report\n")
    file.write("=========================\n\n")
    file.write(f"Total Employees : {len(calculated_bonus)}\n")
    file.write(f"Total Salary    : {total_salary}\n")
    file.write(f"Average Salary  : {average_salary:.2f}\n")
    file.write(f"Highest Salary  : {highest_salary['name']} ({highest_salary['salary']})\n")
    file.write(f"Lowest Salary   : {lowest_salary['name']} ({lowest_salary['salary']})\n")

print("Summary report exported successfully!")