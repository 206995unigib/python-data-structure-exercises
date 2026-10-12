# This program interactively asks about your exam marks, and reports the
# corresponding grades.
#
# Usage:
#
# $ python exam_results.py
#
# A session with the program might look like the following:
#
# $ python exam_results.py
# What marks did you get in Maths?
# > 63
# What marks did you get in Philosophy?
# > 54
# What marks did you get in Geography?
# > 71
# What marks did you get in Music?
# > 68
#
# Your grades:
#
# Maths: B
# Philosophy: C
# Geography: A
# Music: B

diccc = {}
subjects = ['Maths', 'Philosophy', 'Geography', 'Music']

grade_boundaries = {
    'A': [70, 100],
    'B': [60, 69],
    'C': [50, 59],
    'D': [40, 49],
    'E': [30, 39],
    'F': [0, 29],
}

print('This program will ask you your marks in the following subjects:')
#for subject in subjects:
 #   print(' * {}'.format(subject))

for sub in subjects:
    grade = int(input(f'Grade for the course: {sub}: '))
    diccc[sub] = grade

for ke, va in diccc.items():
    for k,v in grade_boundaries.items():
        if va >= v[0] and va <= v[1]:
            print(f'{ke}: {k}')
            break
        
print(diccc)




# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Modify the program to handle the case where the user enters an invalid mark
#   (such as 150, or -25.5, or "bananas")
# * Modify the program to ask the user for the subjects that they've taken.
