#!/usr/bin/env python3
# Python Basics for DevOps

# 1. Variables and Data Types
name = "Srikanth"
age = 25
is_engineer = True
skills = ["Python", "Bash", "Git"]

print(f"Name: {name}, Age: {age}")
print(f"Skills: {skills}")

# 2. Functions
def greet(person_name):
    return f"Hello, {person_name}!"

print(greet(name))

# 3. Loops
print("\n=== Loop Example ===")
for skill in skills:
    print(f"- {skill}")

# 4. Conditionals
if age >= 21:
    print(f"{name} is an adult")
else:
    print(f"{name} is not an adult")

# 5. Dictionary
person = {
    "name": "Srikanth",
    "role": "DevOps Engineer",
    "experience": "2 years"
}

print(f"\nPerson Info: {person}")

# 6. Error Handling
try:
    result = 10 / 2
    print(f"Division result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
