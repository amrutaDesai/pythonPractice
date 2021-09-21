import re

# find Agent followed by a word whoch is name
str = 'Agent Alice gave all the secret documents to Agent Bob'
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall(str))
# O/P ['Agent Alice', 'Agent Bob']

# find and replace(substitute) :- substitute method the sub methid
print(nameRegex.sub('REDACTED',str))
# O/P REDACTED gave all the secret documents to REDACTED

# substitute part of the string of regex like Agent Alice to Agent A****
nameSubRegex = re.compile(r'Agent (\w)\w*')
print(nameSubRegex.sub(r'Agent \1****',str))
# \1 means 1st group in the regex pattern, the first group in the regex is (\w)

" verbose regular expression string:- can add the comments to understand regulat expression strings easily " \
"verbose helps us to make it readable"

""" for example"""
phoneNumberRegex = re.compile(r'''
                           \d\d\d           # area code
                           -                # first dash
                           \d\d\d           # first 3 digits
                           -                # seconf dash
                           \d\d\d\d         # last 4 digits
                        ''',re.VERBOSE)

# even multiple argumentss can be added to a regular expression string

phoneNumberRegex = re.compile(r'''
                           \d\d\d           # area code
                           -                # first dash
                           \d\d\d           # first 3 digits
                           -                # seconf dash
                           \d\d\d\d         # last 4 digits
                        ''',re.VERBOSE | re.IGNORECASE | re.DOTALL )