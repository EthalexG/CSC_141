#Assignment 5
#5-1
# Define a variable
car = 'subaru'

# Test 1 - True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

# Test 2 - False
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

# Test 3 - True
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # True

# Test 4 - False
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')  # False

# Test 5 - True (check lowercase)
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')  # True

# Test 6 - False (case-sensitive check)
print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')  # False

# Test 7 - True (length check)
print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)  # True

# Test 8 - False (wrong length)
print("\nIs len(car) == 5? I predict False.")
print(len(car) == 5)  # False

# Test 9 - True (check if string starts with)
print("\nDoes car start with 'sub'? I predict True.")
print(car.startswith('sub'))  # True

# Test 10 - False (check if string ends with)
print("\nDoes car end with 'z'? I predict False.")
print(car.endswith('z'))  # False

#5-2
# Tests for equality and inequality with strings
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("Is fruit != 'banana'? I predict True.")
print(fruit != 'banana')

print("Is fruit == 'Apple'? I predict False.")
print(fruit == 'Apple')

# Tests using the lower() method
name = 'Alice'
print("Is name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("Is name.lower() == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')  # False

# Numerical tests
age = 25
print("Is age == 25? I predict True.")
print(age == 25)

print("Is age != 30? I predict True.")
print(age != 30)

print("Is age > 20? I predict True.")
print(age > 20)

print("Is age < 20? I predict False.")
print(age < 20)

print("Is age >= 25? I predict True.")
print(age >= 25)

print("Is age <= 24? I predict False.")
print(age <= 24)

# Tests using and/or
score = 85
print("Is score > 80 and score < 90? I predict True.")
print(score > 80 and score < 90)

print("Is score < 80 or score > 90? I predict False.")
print(score < 80 or score > 90)

# Test whether an item is in a list
colors = ['red', 'green', 'blue']
print("Is 'green' in colors? I predict True.")
print('green' in colors)

# Test whether an item is not in a list
print("Is 'yellow' not in colors? I predict True.")
print('yellow' not in colors)

#5-3
# Version that passes the test
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

# Version that fails (no output)
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")

#5-4
# Version where the if block runs
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points.")

# Version where the else block runs
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points.")

#5-5
# Green alien
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# Yellow alien
alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# Red alien
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

#5-6
age = 30  # You can change this value to test other stages

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

#5-7
favorite_fruits = ['banana', 'mango', 'apple']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")

#5-8
usernames = ['admin', 'jaden', 'sarah', 'tony', 'alex']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

#5-9
usernames = []  # Start with an empty list

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
   
#5-10
current_users = ['john', 'sarah', 'mike', 'admin', 'lucy']
new_users = ['Mike', 'LUCY', 'emily', 'bruce', 'chris']

# Convert current users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a new one.")
    else:
        print(f"The username '{new_user}' is available.")

#5-11
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

#5-12
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")


#5-13
#Maybe a simple quiz kinda game can be made like this or one of those text based games you find on like reddit
#You could probably make like a miniature Gradebook
#Making to do lists or Journal apps