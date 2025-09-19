#Ethan Gomez
# 3-1. Names
names = ["Alice", "Bob", "Charlie"]
print(names[0])
print(names[1])
print(names[2])

# 3-2. Greetings
for name in names:
    print(f"Hello {name}, hope you're having a great day!")

# 3-3. Your Own List
transportation = ["Tesla Model S", "Ducati Monster", "Ford Mustang"]
for vehicle in transportation:
    print(f"I would like to own a {vehicle}.")

# 3-4. Guest List
guests = ["Albert Einstein", "Ada Lovelace", "Nikola Tesla"]
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

# 3-5. Changing Guest List
print(f"\nUnfortunately, {guests[1]} can't make it to dinner.")
guests[1] = "Marie Curie"
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner at my place.")

# 3-6. More Guests
print("\nGreat news! I found a bigger dinner table.")
guests.insert(0, "Leonardo da Vinci")
guests.insert(2, "Isaac Newton")
guests.append("Galileo Galilei")
for guest in guests:
    print(f"Dear {guest}, you're invited to dinner at my place.")

# 3-7. Shrinking Guest List
print("\nBad news: the new dinner table won't arrive in time. I can invite only two people.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner this time.")

for guest in guests:
    print(f"{guest}, you're still invited to dinner!")

del guests[0]
del guests[0]
print(f"\nFinal guest list: {guests}")  # Should print an empty list

# 3-8. Seeing the World
places = ["Tokyo", "Reykjavik", "Cairo", "Barcelona", "Cape Town"]
print("Original list:", places)

print("Alphabetical order:", sorted(places))
print("Still original list:", places)

print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Still original list again:", places)

places.reverse()
print("Reversed list:", places)

places.reverse()
print("Back to original order:", places)

places.sort()
print("Sorted alphabetically:", places)

places.sort(reverse=True)
print("Sorted reverse-alphabetically:", places)

# 3-9. Dinner Guests
guests = ["Albert Einstein", "Marie Curie", "Nikola Tesla", "Leonardo da Vinci", "Isaac Newton", "Galileo Galilei"]
print(f"\nI am inviting {len(guests)} people to dinner.")

# 3-10. Every Function
languages = ["Japanese", "Spanish", "Zulu", "Mandarin", "Icelandic"]
print("\nOriginal list:", languages)

# Accessing elements
print("First language:", languages[0])
print("Last language:", languages[-1])

# Adding items
languages.append("Swahili")
print("After append:", languages)

# Inserting items
languages.insert(2, "French")
print("After insert:", languages)

# Removing items
del languages[3]
print("After del:", languages)

popped_language = languages.pop()
print("Popped language:", popped_language)
print("After pop:", languages)

languages.remove("French")
print("After remove:", languages)

# Sorting
print("Sorted list:", sorted(languages))
print("Reverse sorted:", sorted(languages, reverse=True))

# Reversing
languages.reverse()
print("Reversed list:", languages)

# Length
print("Number of languages:", len(languages))

# 3-11. Intentional Error
print("\nIntentional Index Error:")
try:
    print(languages[10])  # This will raise an IndexError
except IndexError:
    print("Oops! Tried to access an index that doesn't exist.")

# Correcting the error
print("Corrected access:", languages[-1])