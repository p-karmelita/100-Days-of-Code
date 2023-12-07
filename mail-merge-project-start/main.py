PLACEHOLDER = '[name]'


with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    print(names)

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)
