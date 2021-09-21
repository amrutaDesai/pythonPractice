import re


phoneNUmRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# \d\d\d-\d\d\d-\d\d\d\d this is called as Regular expression string
#matched Objects
mo = phoneNUmRegex.search('You can call on number 455-555-1234')
print(mo.group())

# Find all occurrences
tmo = phoneNUmRegex.findall('You can call on number 455-555-1234 or 455-565-9876')
print(tmo)
