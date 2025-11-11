# city_functions.py

def city_country(city, country, population=None):
    """Return a neatly formatted city, country string, with optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

