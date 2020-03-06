python
comment


# Addition
a = 6
b = 4
s = a + b
print(s)

# Subtraction
a = 100
b = 80
s = a - b
print(s)

# Multiplication
a = 9
b = 8
s = a * b
print(s)

# Division
a = 200
b = 24
s = a / b
print(s)

# Exponents

a = 8
b = 4
s = a ** b
print(s)

"""
These
are
multi-line
comments
"""

# String and Numeric Data Types

a = "I ate a banana"
type(a)
print(a)

a = 123
type(a)
print(a)

a = 98.6
type(a)
print(a)

a = "hello"
b = "everyone"
c = a + " " + b
print(c)

d = a  * 8
print(d)

a = 137
print(float(a))

a = 596.89
print(int(a))

a = "42.97"
print(float(a))

""" Variables
I used variables above
"""

dogs = 40
cats = 25
rabbits = 10

shelter_lenght = 30
shelter_widht = 25

total_animals = dogs + cats + rabbits
sqft = shelter_lenght * shelter_widht

print("Total number of animals:" , total_animals)
print("Total shelter square feet:", sqft)
print("Square feet per animal:", sqft/total_animals)

# Accepting Variable Inputs
first_name = input("Enter your first name: ")
print("Hello,", first_name + "!")



dogs = int(input("Enter the number of dogs: "))
cats = int(input("Enter the number of cats: "))
rabbits = int(input("Enter the number of rabbits: "))
shelter_length = int(input("Enter the shelter length: " ))
shelter_width = int(input("Enter the shelter width: " ))

total_animals = dogs + cats + rabbits
sqft = shelter_length * shelter_width

print("Total number of animals:", total_animals)
print("Total shelter square feet:", sqft)
print("Square feet per animal:", sqft/total_animals)

# Counting and Indexing
a = "automobile"
print(len(a))

a = "automobile"
print(a[0])

a = "automobile"
print(a[1])

a = "automobile"
print(a[9])

a = "automobile"
print(a[-1])

a = "automobile"
print(a[-2])

a = "automobile"
print(a[:4])

a = "automobile"
print(a[4:])

a = "automobile"
print(a[3:8])

