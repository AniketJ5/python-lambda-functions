# regular function
def calculate_bonus(salary): 
    return salary * 0.10
    
print(calculate_bonus(50000))

# lambda function
calculate_bonus = lambda salary: salary * 0.10

print(calculate_bonus(50000))
