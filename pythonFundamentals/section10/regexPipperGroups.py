import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Your phone number is 455-555-1234')
print(mo)
# <re.Match object; span=(21, 33), match='455-555-1234'>

print(mo.group())

# groups can be found

phoneNumberRegexGroup = re.compile((r'(\d\d\d)-(\d\d\d-\d\d\d\d)'))
mo = phoneNumberRegexGroup.search('Your phone number is 455-555-1234')
print(mo.group(1))
print(mo.group(2))


print(' Pipe regex '.center(20,'*'))
# Pipe in regex can be used to find possible suffix in the string

batgerex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batgerex.search('Batmobile is wondering here n there')
print(mo.group())
print(mo.group(1)) # to find which suffix is found from all possible siffxes 