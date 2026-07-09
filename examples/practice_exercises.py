# ETL Scenario with lambda function and understanding of kwargs

# Extract Stage
records = [
    {"name": "John", "salary": 50000},
    {"name": "Alice", "salary": 60000},
    {"name": "Bob", "salary": 45000}
]

# Transform stage
# We want to calculate a 10% bonus for each employee before loading the data.
updated = list(
    map(
        lambda r: {
            **r,
            "bonus": r["salary"] * 0.10
        },
        records
    )
)

print(updated)