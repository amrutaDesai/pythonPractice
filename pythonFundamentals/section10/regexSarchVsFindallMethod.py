import re

message = 'you can call me on number 445-555-1234'
phoneregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneregex.search(message)
print(' Plain regex '.center(20,'*'))
print(mo)
# serach finds 1 object or 1st match in the message
# O/P <re.Match object; span=(26, 38), match='445-555-1234'>

# findall() method on regex object will find all the matched objects
# if the regex is simple plain object without group it will return list of matched objects
message1 = 'you can call me on number 445-555-1234 OR 445-231-2345'
mo =phoneregex.findall(message1)
print(' findall() method & regex defined as plain object'.center(20,'*'))
print(mo)
# O/P ['445-555-1234', '445-231-2345']


# If the regex is defined in groups then it returns the list of tuples
phoneregex = re.compile(r'((\d\d\d)-\d\d\d-\d\d\d\d)')
mo = phoneregex.findall(message1)
print(' Regex object defined in a 2 group '.center(20,'*'))
print(mo)
# O/P [('445-555-1234', '445'), ('445-231-2345', '445')]
"""
as there are 2 groups 
1. (\d\d\d)
2. ((\d\d\d)-\d\d\d-\d\d\d\d)

O/P returns the tuples of 2 strings ('445-555-1234', '445')

"""

# If the regex is defined in groups then it returns the list of tuples
phoneregex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo = phoneregex.findall(message1)
print(' Regex object defined in a 3 group '.center(20,'*'))
print(mo)
# O/P [('445-555-1234', '445', '555-1234'), ('445-231-2345', '445', '231-2345')]
"""
as there are 3 groups 
1. (\d\d\d)
2. (\d\d\d-\d\d\d\d)
2. ((\d\d\d)-(\d\d\d-\d\d\d\d))

O/P returns the list of tuples with 3 strings ('445-555-1234', '445', '555-1234')
"""