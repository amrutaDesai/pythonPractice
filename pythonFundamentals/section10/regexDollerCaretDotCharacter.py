import re

"""

 ^ the string must begins with something
 $ the string must ends with something
 . any character except newline 
 . is greedy matchers so get as much as possible
"""


msg = 'Hello there!'
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search(msg))

msg2 = 'He said "Hello there" '
print(beginsWithHelloRegex.search(msg2))

msg3 = 'Hello world'
endsWithHelloRegex = re.compile(r'world$')
print(endsWithHelloRegex.search(msg3))

# full number
beginEndsWithRegex = re.compile(r'^\d+$')
print(beginEndsWithRegex.search('1231431423423423423'))
print(beginEndsWithRegex.search('1231431423423423x23'))

msg1 = 'The cat in the hay ssat on the flat mat'
atRegex = re.compile(r'.at')
print(atRegex.findall(msg1))

# as .at has oone character before at so the word lat has been displayed and not flat

atRegex = re.compile(r'.{1,2}at') # anything 1 or 2 letters
print(atRegex.findall(msg1))

# so flat will be included in the output


str='First Name: Al Last Name: Sweigart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(str))


# nongreedy match of .
serve = '<To server Humans> for dinner>'
nonGreedyRegex = re.compile(r'<(.*?)>') # find out as little as possible which starts with < and ends with >
print(nonGreedyRegex.findall(serve))

# greedy match of .
nonGreedyRegex = re.compile(r'<(.*)>') # find out as much as possible which starts with < and ends with >
print(nonGreedyRegex.findall(serve))
# the last dinner ends with > so greedy match included whole thing


# match  anything except new line '.'
serve = 'Server public trust.' + "\n" +'Protect the innocent.'
dotstarRegex = re.compile(r'.*')
print(dotstarRegex.search(serve))

# . means literally anything except new line but re.DOTALL will also new line
dotstarRegex = re.compile(r'.*', re.DOTALL)
print(dotstarRegex.search(serve))

# ignore case upper or lower
str = 'Al, where is programming book you talk about Robocop a lot'
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall(str))
# O/p finds all lower case vowels fromthe string

# ignore case and find all
vowelNonCaseSensetiveRegex = re.compile(r'[aeiou]',re.IGNORECASE) # re.I shortcut
print(vowelNonCaseSensetiveRegex.findall(str))