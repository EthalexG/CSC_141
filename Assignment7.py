#Assignment 7 >:3
#7-1
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")

#7-2
group_size = int(input("How many people are in your dinner group? "))

if group_size > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

#7-3
number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

#7-4
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
print("Finished making your pizza!")

#7-5
while True:
    age = input("Enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    if price == 0:
        print("Your ticket is free!")
    else:
        print(f"Your ticket costs ${price}.")

#7-6
topping = ''
while topping != 'quit':
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
print("Finished making your pizza!")
active = True
while active:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")
print("Finished making your pizza!")

#7-7
while True:
    print("This loop will run forever! Press CTRL-C to stop it.")

#7-8
    sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#7-9
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made (no pastrami):")
for sandwich in finished_sandwiches:
    print(sandwich)

#7-10
responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = place
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
