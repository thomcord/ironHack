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

# Lists

lst = ['The', 'man', 'in', 'the', 'blue', 'suit']
print(lst[0])
print((lst[1]))
print(lst[-1])
print(lst[2:4])

lst.append('jacket')
print(lst)

lst.remove('suit')
print(lst)

lst2 = ['and', 'the', 'green', 'trousers']
comb_list = lst + lst2
print(comb_list)

nested = [['A', 'man'], ['a', 'plan'], ['a', 'canal'], ['Panama', '!']]
print(nested[0])
print(nested[0][1])
print(nested[-1][0])

num_list = [34, 12, 93, 783, 330, 896, 1, 55]
#sum
print(sum(num_list))
#mean
print(sum(num_list)/len(num_list))
#minimun
print(min(num_list))
#maximum
print(max(num_list))

#Sort Ascending
num_list.sort()
print(num_list)

#Sort descending
num_list.sort(reverse=True)
print(num_list)

#Reversing
num_list.reverse()
print(num_list)


#Dictionaries

ages = {'Brian':23, 'Amy':22, 'Darlene':47, 'Ralph':32, 'Jordan':28, 'Stephanie':35}
print(ages['Brian'])

print(ages['Stephanie'])

print(ages.keys())

print(ages.values())

ages['Vanessa']=30
print(ages)

del ages['Vanessa']
print(ages)

#Tuples

a = [1,2,3,4,5]
b = (1,2,3,4,5)

a.append((6))
print(a)

#b.append(6)
#It is not possible to .append() on tuples

a.remove(2)
print(a)

#b.remove(2)
#It is not possible to .remove() on tuples

a.sort()
print(a)

#b.sort()
#It is not possible to .sort() on tuples

tuple(a)
print(a)

list(b)
print(b)

#Sets

dupe_list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
uniques = set(dupe_list)
print(uniques)

list(uniques)
print(uniques)

#Boolean Data Types

happy=True
print("Happy variable is set to ", happy)

print(5 + 5 == 10)
print('apple' != 'orange')
print(100 > 75)
print(93 < 80)
print(3 in [1,2,3,4,5])
print(3 not in [1,2,3,4,5])


print((5 + 5 == 10) & ('apple' != 'orange'))
print((100 > 75) & (93 < 80))
print((100 > 75) | (93 < 80))
print((93 < 80) | (3 not in [1,2,3,4,5]))

#Conditional Logic

number = 10

if number<10:
    print("Numer is less than 10")
elif number> 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly 10")
else:
    print("Number is probably not a numbe at all")

commute = 30
rain = False
traffic = True

if (rain == True) | (traffic == True):
    if (rain == True) & (traffic == True):
        total_commute = commute + 15 + 20
    elif (rain == True) & (traffic == False):
        total_commute = commute + 15
    elif (rain == False) & (traffic == True):
        total_commute = commute + 20
else:
    total_commute = commute
print("Your total commute time is expected to be", total_commute, "minutes.")

#For loops
range(5, 15)
len(range(5, 15))

for i in range(5, 15):
    print(i)

fruits = ['apple', 'orange', 'banana', 'grapes', 'pineapple']

for fruit in fruits:
    print(fruit)

ages = {'Brian':23, 'Amy':22, 'Darlene':47, 'Ralph':32, 'Jordan':28, 'Stephanie':35}

for name, age in ages.items():
    print(name, "is", age, "years old.")

num_list = [34, 12, 93, 783, 330, 896, 1, 55]

total = 0

for i in num_list:
    total += i
    print("Total is currently", total)

new_list = []

for i in range(1, 11):
    square = i**2
    new_list.append(square)

print(new_list)

total_time = 60
minutes_elapsed = 0
wait = 15

print("Cake is in the oven.")
minutes_elapsed += wait

while minutes_elapsed < total_time:
    print("Cake is not done yet.")
    minutes_elapsed += wait

print("It's done. Let's eat cake!")
