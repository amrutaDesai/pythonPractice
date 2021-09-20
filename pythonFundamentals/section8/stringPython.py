def stringNotes():
    print('''1. String can begin and ends with double quotes
    2. Escape characters let you put qutoes and other characters that are hard to type inside strings
    3. Raw strings will literally print any backslashes in the string and ignore escape characters
    4. multiline string and begin and end with three quotes and can span mulitle lines
    5. INdexes slices and the in or not in operators all works with strings 
    ''')

def stringSomeMOreNotes():
    print("""
    1.upper() and lower() return an uppercase or lowercase string.
    2.isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns True or False 
    if the string is that uppercase, lowercase, alphabetical letters, and so on.
    3.startswith() and endswith() also return bools.
    4.‘,'.join([‘cat', ‘dog']) returns a string that combines the strings in the given list.
    5.Hello world'.split() returns a list of strings split from the string it's called on.
    6.rjust() ,ljust(), center() returns a string padded with spaces.
    7.strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
    8.replace() will replace all occurrences of the first string argument with the second string argument.
    9.Pyperclip has copy() and paste() functions for getting and putting strings on the clipboard.
    10. String can be formatted with %s """)

def strinfFormatting():
    name = 'Alice'
    place = 'Main Stream'
    time = '6 pm'
    food = 'tunips'
    print('Hello '+ name + ' you are invited to a party '+ place + ' at ' + time + '. Please bring '+ food +
          '.')
    print('Helle {} you are invited to a party {} at {}. please bring {}'.format(name,place,time,food))


## ?????
print('SpamSamBeconSpamEggsSpamSpam'.strip('ampS'))
stringNotes()
stringSomeMOreNotes()
strinfFormatting()