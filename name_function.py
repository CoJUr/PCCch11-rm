"""
A simple function for testing purposes that takes in a first and last name
and returns a full name
"""


# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()
#
# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted full name which will have a middle name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name which CAN have a middle name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()



