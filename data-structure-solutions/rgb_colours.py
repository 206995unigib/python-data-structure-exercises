# This program knows about the RGB code corresponding to common colours.
#
# Usage:
#
# $ python rgb_colours.py [colour]
#
# For instance:
#
# $ python rgb_colours.py red
# The RGB code for red is F00
#
# or:
#
# $ python rgb_colours.py "burnt sienna"
# I don't know the RGB code for burnt sienna


colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]


# c = input('What is your color (name)? ')
# for color in colours:    
#     if c == color[0]:
#         print(f'Your color tag: {color[1]}')


def pick_color(name):
    for color in colours:
        if name == color[0]:
            return color[1]

print(pick_color('blue'))





# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that users can also enter an RGB colour code, and be
#   told the name of the corresponding colour.
# * Change the program so that it ignores the case of the user's input.
