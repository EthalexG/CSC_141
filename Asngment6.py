#Assignment 6 :D
#6-1
person = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'New York'
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

#6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 3,
    'Charlie': 9,
    'Diana': 5,
    'Eve': 1
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

#6-3
glossary = {
    'variable': 'A reserved memory location to store values.',
    'loop': 'A sequence of instructions that repeats until a condition is met.',
    'function': 'A block of reusable code that performs a specific task.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'An ordered collection of items.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

#6-4
glossary.update({
    'tuple': 'An immutable ordered list.',
    'set': 'A collection of unique elements.',
    'class': 'A blueprint for creating objects.',
    'method': 'A function that is associated with an object.',
    'module': 'A file containing Python definitions and statements.'
})

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

#6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nList of rivers:")
for river in rivers.keys():
    print(river.title())

print("\nList of countries:")
for country in rivers.values():
    print(country.title())

#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'michael', 'sarah', 'david', 'edward']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take the favorite languages poll!")

#6-7
person1 = {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28, 'city': 'New York'}
person2 = {'first_name': 'Bob', 'last_name': 'Smith', 'age': 35, 'city': 'Chicago'}
person3 = {'first_name': 'Charlie', 'last_name': 'Brown', 'age': 22, 'city': 'San Francisco'}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name']} {person['last_name']}, Age: {person['age']}, City: {person['city']}")


#6-8
pet1 = {'animal': 'dog', 'owner': 'Alice'}
pet2 = {'animal': 'cat', 'owner': 'Bob'}
pet3 = {'animal': 'parrot', 'owner': 'Charlie'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner']} owns a {pet['animal']}.")

#6-9
favorite_places = {
    'alice': ['paris', 'tokyo'],
    'bob': ['new york'],
    'charlie': ['london', 'berlin', 'rome']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")
    print()

#6-10
favorite_numbers = {
    'alice': [7, 3, 22],
    'bob': [9],
    'charlie': [1, 5]
}

for name, numbers in favorite_numbers.items():
    numbers_str = ", ".join(str(num) for num in numbers)
    print(f"{name.title()}'s favorite numbers are: {numbers_str}")

#6-11
cities = {
    'new york': {
        'country': 'usa',
        'population': '8 million',
        'fact': 'Known as the Big Apple.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'Famous for its cherry blossoms.'
    },
    'paris': {
        'country': 'france',
        'population': '2 million',
        'fact': 'Home to the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")

#6-12
cities['new york']['famous_food'] = 'Bagels'
cities['tokyo']['famous_food'] = 'Sushi'
cities['paris']['famous_food'] = 'Croissants'

for city, info in cities.items():
    print(f"{city.title()}:")
    for key, value in info.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()
