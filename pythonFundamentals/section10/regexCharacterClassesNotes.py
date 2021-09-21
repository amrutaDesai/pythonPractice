# Character class
def tabelCommonCharacterClass():
    print('-'.center(150,'-'))
    print('Shorthand Character Class'.ljust(50,' ') + 'Represents'.ljust(50,' '))
    print('\d'.ljust(50,' ') + 'Any numeric digit from 0 to 9.'.ljust(50,' '))
    print('\D'.ljust(50,' ') + 'Any character that is not a numeric digit from 0 to 9.'.ljust(50,' '))
    print('\w'.ljust(50,' ') + 'Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)'.ljust(50,' '))
    print('\W'.ljust(50,' ') + 'Any character that is not a letter, numeric digit, or the underscore character.'.ljust(50,' '))
    print('\s'.ljust(50,' ') + 'Any space, tab, or newline character. (Think of this as matching “space” characters.)'.ljust(50,' '))
    print('\S'.ljust(50,' ') + 'Any character that is not a space, tab, or newline.'.ljust(50,' '))
    print('-'.center(150,'-'))




def notes():
    print("""
1.The regex method findall() is passed a string, and returns all matches in it, not just 	the first match.
2.If the regex has 0 or 1 group, findall() returns a list of strings.
3.If the regex has 2 or more groups, findall() returns a list of tuples of strings.
	\d is a shorthand character class that matches digits. \w matches "word 		characters" (letters, numbers, and the underscore). \s matches whitespace 		characters (space, tab, newline).
4.The uppercase shorthand character classes \D, \W, and \S match charaters that are not 	digits, word characters, and whitespace.
5.You can make your own character classes with square brackets: [aeiou]
6.A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]
""")
notes()
tabelCommonCharacterClass()