# 4-1: Favorite Pizzas
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")


# 4-2: Animals
animals = ['Dog', 'Cat', 'Rabbit']

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals would make a great pet!")


# 4-3: Counting to Twenty
for number in range(1, 21):
    print(number)


# 4-4: One Million (⚠️ Huge output — commented out for safety)
# million_numbers = list(range(1, 1000001))
# for number in million_numbers:
#     print(number)


# 4-5: Summing a Million
million_numbers = list(range(1, 1000001))

print(f"Minimum value: {min(million_numbers)}")
print(f"Maximum value: {max(million_numbers)}")
print(f"Sum of all numbers: {sum(million_numbers)}")


# 4-6: Odd Numbers from 1 to 20
for number in range(1, 21, 2):
    print(number)


# 4-7: Multiples of 3 from 3 to 30
for number in range(3, 31, 3):
    print(number)


# 4-8: First 10 Cubes
for number in range(1, 11):
    print(f"The cube of {number} is {number ** 3}")


# 4-9: Cube Comprehension
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)


# 4-10: Pizza List Slices
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken',
          'Hawaiian', 'Vegetarian']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

print("\nThe first three items in the list are:")
print(pizzas[:3])

middle_index = len(pizzas) // 2
print("\nThree items from the middle of the list are:")
print(pizzas[middle_index - 1:middle_index + 2])

print("\nThe last three items in the list are:")
print(pizzas[-3:])


# 4-11: My Pizzas, Your Pizzas
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']
friend_pizzas = pizzas[:]

pizzas.append('Hawaiian')
friend_pizzas.append('Vegetarian')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


# 4-12: More Loops — Foods and Desserts
foods = ['Pizza', 'Burger', 'Pasta', 'Sushi', 'Salad']

print("My favorite foods are:")
for food in foods:
    print(food)

desserts = ['Ice Cream', 'Cake', 'Pie', 'Brownie']

print("\nMy favorite desserts are:")
for dessert in desserts:
    print(dessert)
