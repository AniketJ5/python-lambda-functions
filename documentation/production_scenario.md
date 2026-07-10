# Production Scenario: Processing 30 Million Customer Records Using Lambda Functions

## Scenario

A retail company processes **30 million customer records every day** through an ETL (Extract, Transform, Load) pipeline before loading data into a Data Warehouse.

### Business Requirements

- Read customer records
- Filter only **Active** customers
- Calculate discounts based on membership
- Sort customers by purchase value
- Transform records into warehouse format
- Keep the code efficient, readable, and maintainable

---

# Sample Input

```python
customers = [
    {
        "customer_id": 101,
        "name": "Alice",
        "status": "Active",
        "membership": "Gold",
        "purchase_value": 25000
    },
    {
        "customer_id": 102,
        "name": "Bob",
        "status": "Inactive",
        "membership": "Silver",
        "purchase_value": 18000
    },
    {
        "customer_id": 103,
        "name": "Charlie",
        "status": "Active",
        "membership": "Regular",
        "purchase_value": 12000
    }
]
```

---

# ETL Pipeline

```
Extract
      │
      ▼
Read Customer Records
      │
      ▼
Filter Active Customers
      │
      ▼
Calculate Discounts
      │
      ▼
Transform Records
      │
      ▼
Sort by Purchase Value
      │
      ▼
Load into Data Warehouse
```

---

# Step 1 : Filter Active Customers

Since filtering is a simple condition, a lambda expression is a good choice.

```python
active_customers = list(
    filter(
        lambda customer: customer["status"] == "Active",
        customers
    )
)
```

### Why use lambda?

- Only one condition
- Easy to understand
- No extra reusable logic
- Very common in ETL pipelines

Result

```
Alice
Charlie
```

---

# Step 2 : Calculate Discounts

### Business Rule

| Membership | Discount |
|------------|----------|
| Gold | 20% |
| Silver | 10% |
| Regular | 5% |

Many beginners write this using a long lambda.

```python
discounted = list(
    map(
        lambda customer: {
            **customer,
            "discount":
                customer["purchase_value"] * 0.20
                if customer["membership"] == "Gold"
                else customer["purchase_value"] * 0.10
                if customer["membership"] == "Silver"
                else customer["purchase_value"] * 0.05
        },
        active_customers
    )
)
```

Although this works, it is **not recommended** for production because the business logic is hidden inside a lambda.

---

# Better Approach

Move the business logic into a regular function.

```python
def calculate_discount(customer):

    membership = customer["membership"]

    if membership == "Gold":
        discount = customer["purchase_value"] * 0.20

    elif membership == "Silver":
        discount = customer["purchase_value"] * 0.10

    else:
        discount = customer["purchase_value"] * 0.05

    return {
        **customer,
        "discount": discount
    }
```

Now use the function inside `map()`.

```python
discounted = list(
    map(
        calculate_discount,
        active_customers
    )
)
```

### Why is this better?

- Easy to read
- Easy to debug
- Easy to test
- Business logic is reusable
- New discount rules can be added without changing the pipeline

---

# Step 3 : Sort by Purchase Value

Sorting is another perfect place for lambda.

```python
sorted_customers = sorted(
    discounted,
    key=lambda customer: customer["purchase_value"],
    reverse=True
)
```

### Why?

The lambda simply tells Python which field should be used for sorting.

---

# Step 4 : Transform Records

Before loading data into the warehouse, we only keep required fields.

```python
warehouse_records = list(
    map(
        lambda customer: {
            "customer_id": customer["customer_id"],
            "customer_name": customer["name"].upper(),
            "purchase_value": customer["purchase_value"],
            "discount": round(customer["discount"], 2)
        },
        sorted_customers
    )
)
```

Example Output

```python
{
    "customer_id": 101,
    "customer_name": "ALICE",
    "purchase_value": 25000,
    "discount": 5000
}
```

This is the final dataset loaded into the Data Warehouse.

---

# Where Would You Use Lambda Functions?

Use lambda functions for **simple, one-line operations**.

Examples

Filtering

```python
filter(lambda customer: customer["status"] == "Active", customers)
```

Sorting

```python
sorted(customers, key=lambda customer: customer["purchase_value"])
```

Simple Transformation

```python
map(lambda customer: customer["name"].upper(), customers)
```

Selecting a Field

```python
lambda customer: customer["salary"]
```

Simple Calculations

```python
lambda price: price * 1.18
```

---

# When Would You Prefer Regular Functions?

Use a regular function when:

- Business logic is complex
- Multiple conditions are involved
- Error handling is required
- Logging is needed
- Logic is reused
- Unit testing is required

Example

```python
def calculate_discount(customer):
    ...
```

This is much easier to maintain than embedding all the logic inside a lambda.

---

# How Would You Improve Code Readability?

## 1. Keep lambda expressions short

Good

```python
lambda customer: customer["status"] == "Active"
```

Bad

```python
lambda customer:
    if...
    elif...
    else...
```

---

## 2. Use meaningful variable names

Good

```python
lambda customer: customer["purchase_value"]
```

Bad

```python
lambda x: x["purchase_value"]
```

---

## 3. Move business logic into helper functions

Good

```python
discounted = map(calculate_discount, customers)
```

---

## 4. Avoid nested conditional expressions

Instead of

```python
lambda ...
```

use

```python
def calculate_discount():
```

---

## 5. Write code for humans

Production code is maintained by teams.

Readable code is more valuable than writing fewer lines.

---

# Performance Considerations

For **30 million records**, avoid converting everything into lists.

Instead of

```python
list(filter(...))
```

prefer lazy evaluation.

```python
active_customers = filter(
    lambda customer: customer["status"] == "Active",
    customers
)

discounted = map(
    calculate_discount,
    active_customers
)
```

This processes records one by one instead of loading all records into memory.

For very large datasets, Data Engineers typically use:

- PySpark DataFrames
- Pandas (for smaller datasets)
- Apache Beam
- Dask
- Databricks
- SQL transformations

instead of Python lists.

---

# Interview Answer

> In a production ETL pipeline processing millions of customer records, I use lambda functions for short, single-expression operations such as filtering active customers, sorting by purchase value, or simple field transformations. If the business logic becomes complex, such as calculating discounts with multiple rules, I move that logic into a named function. This improves readability, maintainability, testing, and debugging. For very large datasets, I also avoid unnecessary list creation and prefer lazy evaluation or distributed processing frameworks like PySpark to keep memory usage low and improve scalability.