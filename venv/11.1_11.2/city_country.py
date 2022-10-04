"""
Write a function that accepts two parameters: a city and a country name. It
returns a single string of 'City, Country'
11-2: make the function with a 3rd param, population. New output:
'City, Country - population xxx,xxx.
"""


# def location_stringer(city, country, population):
#     """Return a string like 'City, Country'."""
#     return f"{city.title()}, {country.title()}"


def location_stringer(city, country, population=''):
    """Return a string like 'City, Country'."""
    if population:
        formatted_location = f"{city.title()}, {country.title()}" + \
                         " - population " + f"{population}"
    else:
        formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location

# print(location_stringer('santiago', 'chile', 5000))