# Refactoring Long Lambda Expressions

## Question

**A lambda expression becomes long and difficult to understand. How would you refactor the code for better readability?**

## Answer

A lambda function should be used only for **short, simple, single-expression operations**. If it becomes long or contains complex business logic, refactor it into a **regular named function**.

### Why?

- Improves readability
- Easier to debug
- Easier to test
- Reusable across the application
- Simplifies maintenance

---

## Bad Example (Long Lambda)

```python
discounts = list(
    map(
        lambda c: {
            **c,
            "discount": c["purchase"] * 0.20
            if c["membership"] == "Gold"
            else c["purchase"] * 0.10
            if c["membership"] == "Silver"
            else c["purchase"] * 0.05
        },
        customers
    )
)
```

---

## Good Example (Refactored)

```python
def calculate_discount(customer):
    if customer["membership"] == "Gold":
        discount = customer["purchase"] * 0.20
    elif customer["membership"] == "Silver":
        discount = customer["purchase"] * 0.10
    else:
        discount = customer["purchase"] * 0.05

    return {**customer, "discount": discount}

discounts = list(map(calculate_discount, customers))
```

---

## When to Use Lambda

- Simple filtering (`filter()`)
- Simple sorting (`sorted()`)
- Simple transformations (`map()`)
- One-line calculations

Example:

```python
sorted(employees, key=lambda e: e["salary"])
```

---

## When to Use Regular Functions

- Complex business logic
- Multiple conditions
- Error handling
- Logging
- Code reuse
- Unit testing

---

## Interview Answer

> Lambda functions are ideal for short, single-expression operations. If a lambda becomes complex, I replace it with a named function to improve readability, maintainability, testing, and debugging. In production code, clear and maintainable code is preferred over compact code.