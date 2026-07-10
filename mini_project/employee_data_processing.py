import csv

# -------------------------------
# Read Employee Records
# -------------------------------

employees = [{},{}]

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

print("\nOriginal Employee Records\n")

for emp in employees:
    print(emp)

# -------------------------------
# Transform Employee Names
# -------------------------------

transformed = list(
    map(
        lambda e: {
            **e,
            "name": e["name"].upper()
        },
        employees
    )
)

# -------------------------------
# Filter Employees by Department
# -------------------------------

it_employees = list(
    filter(
        lambda e: e["department"] == "IT",
        transformed
    )
)

# -------------------------------
# Filter Active Employees
# -------------------------------

active = list(
    filter(
        lambda e: e["status"] == "Active",
        it_employees
    )
)

# -------------------------------
# Sort By Salary
# -------------------------------

sorted_emp = sorted(
    active,
    key=lambda e: e["salary"],
    reverse=True
)

# -------------------------------
# Calculate Bonus (10%)
# -------------------------------

bonus_list = list(
    map(
        lambda e: {
            **e,
            "bonus": round(e["salary"] * 0.10, 2)
        },
        sorted_emp
    )
)

# -------------------------------
# Summary Statistics
# -------------------------------

total_salary = sum(map(lambda e: e["salary"], bonus_list))

average_salary = (
    total_salary / len(bonus_list)
    if bonus_list else 0
)

highest_salary = max(
    bonus_list,
    key=lambda e: e["salary"]
)

lowest_salary = min(
    bonus_list,
    key=lambda e: e["salary"]
)

# -------------------------------
# Print Report
# -------------------------------

print("\nProcessed Employees\n")

for emp in bonus_list:
    print(emp)

print("\nSummary Report")
print("----------------------------")
print("Total Employees :", len(bonus_list))
print("Total Salary    :", total_salary)
print("Average Salary  :", round(average_salary, 2))
print("Highest Salary  :", highest_salary["name"], highest_salary["salary"])
print("Lowest Salary   :", lowest_salary["name"], lowest_salary["salary"])

# -------------------------------
# Export Processed Data
# -------------------------------

with open("processed_employees.csv", "w", newline="") as file:

    fields = [
        "employee_id",
        "name",
        "department",
        "salary",
        "status",
        "bonus"
    ]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()
    writer.writerows(bonus_list)

print("\nProcessed data exported successfully!")

# -------------------------------
# Export Summary Report
# -------------------------------

with open("summary_report.txt", "w") as file:

    file.write("EMPLOYEE SUMMARY REPORT\n")
    file.write("=========================\n\n")
    file.write(f"Total Employees : {len(bonus_list)}\n")
    file.write(f"Total Salary    : {total_salary}\n")
    file.write(f"Average Salary  : {average_salary:.2f}\n")
    file.write(f"Highest Salary  : {highest_salary['name']} ({highest_salary['salary']})\n")
    file.write(f"Lowest Salary   : {lowest_salary['name']} ({lowest_salary['salary']})\n")

print("Summary report exported successfully!")