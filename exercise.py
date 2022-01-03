import random

dates = ['Jeferson', 'Matilda', 'R@fael', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M', 'Loquesea']
surnames = ['10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
excuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined']

# 1 - A function that generates a random excuse with this data 

def excuse_generator(surnames, excuses, dates):

    name = dates[random.randint(0, len(dates) - 1)]
    surname = surnames[random.randint(0, len(surnames) - 1)]
    excuse = excuses[random.randint(0, len(excuses) - 1)]

    print(f"My excuse: {name} {surname} {excuse}")


# 2 - A function that counts the number of repetitions of letters in each array.

def letter_counter(list):
    letter_iterations = {}

    for item in list:
        for letter in item:
            letter_iterations[letter.upper()] = letter_iterations.get(letter.upper(), 0) + 1      

    print(f"Dictionary of number of letters: {dict(sorted(letter_iterations.items()))}")


# 3 - A function to remove repetitions in an array and return a clean array without the repetition.
def no_repetitions(list):
    print(f"The list without repetitions is: {set(list)}")


# 4 - A function that inverts all the values of the array
def invert_list(list):
    print (f"List inverted: {list[::-1]}")


excuse_generator(dates, surnames, excuses)
letter_counter(surnames)
no_repetitions(dates)
invert_list(excuses)
