#Assignment 8
#8-1
def display_message():
    print("I'm learning about functions in this chapter.")
# Call the function
display_message()

#8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function with a book title
favorite_book("Alice in Wonderland")

#8-3
def make_shirt(size, message):
    print(f"Making a {size} T-shirt with the message: '{message}' printed on it.")

# Call the function using positional arguments
make_shirt("Large", "Code like a pro!")

# Call the function using keyword arguments
make_shirt(message="Dream big, code bigger!", size="Medium")

#8-4
def make_shirt(size="Large", message="I love Python"):
    print(f"Making a {size} T-shirt with the message: '{message}' printed on it.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a custom shirt with a different size and message
make_shirt(size="Small", message="Keep calm and code on.")

#8-5
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik")
describe_city("Akureyri")
describe_city("Tokyo", country="Japan")

#8-6
def city_country(city, country):
    return f"{city}, {country}"

# Call the function with examples and print the results
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))

#8-7
def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if num_songs is not None:
        album["songs"] = num_songs
    return album

# Make three albums
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Adele", "30", num_songs=12)

# Print the album dictionaries
print(album1)
print(album2)
print(album3)

#8-8
def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if num_songs:
        album["songs"] = num_songs
    return album

# User input loop
print("Enter album information (or type 'quit' to exit):")
while True:
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    num = input("Number of songs (optional - press Enter to skip): ")
    if num.lower() == 'quit':
        break

    if num:
        album = make_album(artist, title, int(num))
    else:
        album = make_album(artist, title)

    print("Album created:", album)
    print()  # Blank line for spacing

    #8-9
    def show_messages(messages):
    for message in messages:
        print(message)

# List of short text messages
messages = ["Hello!", "Good morning!", "How are you?", "See you soon."]

# Call the function
show_messages(messages)

#8-10
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Original list
messages = ["Hello!", "Good morning!", "How are you?", "See you soon."]
sent_messages = []

# Call the function
send_messages(messages, sent_messages)

# Show final lists
print("\nMessages list:", messages)
print("Sent messages list:", sent_messages)

#8-11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Original list
original_messages = ["Hello!", "Good morning!", "How are you?", "See you soon."]
sent_messages = []

# Call the function with a copy of the list
send_messages(original_messages[:], sent_messages)

# Show that the original list is unchanged
print("\nOriginal messages list:", original_messages)
print("Sent messages list:", sent_messages)

#8-12
def make_sandwich(*items):
    print("Making a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

# Call the function three times with different numbers of ingredients
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "tomato")
make_sandwich("peanut butter", "jelly", "banana", "honey")

#8-13
def build_profile(first, last, **user_info):
    profile = {
        "first_name": first,
        "last_name": last
    }
    profile.update(user_info)
    return profile

# Build your profile
my_profile = build_profile(
    "John", "Doe",
    location="New York",
    hobby="coding",
    profession="software engineer"
)

print(my_profile)

#8-14
def make_car(manufacturer, model, **options):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }
    car.update(options)
    return car

# Example call
car = make_car("Tesla", "Model S", color="red", autopilot=True)

print(car)
