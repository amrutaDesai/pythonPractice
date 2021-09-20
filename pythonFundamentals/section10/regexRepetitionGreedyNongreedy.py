# ? : the group before ? can occurred 0 or 1 time
import re

print(' ? : the group before ? can occurred 0 or 1 time '.center(70,'*'))
batRegex = re.compile(r'bat(wo)?man') # wo can occure 0/1 time
mo = batRegex.search('The adventures of batman')
print(mo.group())

mo = batRegex.search('The adventures of batwoman')
print(mo.group())


mo = batRegex.search('The adventures of batwowowowman')
print(mo == None)

# when regex object for the text dinner?

dinnerRegex = re.compile(r'dinner\?') ## dinner is not optional here as there is a \ before? so it is part of text
mo = dinnerRegex.search('Are you coming for dinner?')
print(mo.group())

# matching number of repetition
heRegex = re.compile(r'(Ha){3}')
mo = heRegex.search('He said HaHaHa')
print(mo.group())


phoneNumberRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneNumberRegex.search('Your phone number is 455-555-1234,555-456-1234,234-5678ß')
print(mo)

# looking for repetition in a range like Ha can occure 3 times or 4 or 5
strRegex = re.compile(r'(Ha){3,5}')
mo = strRegex.search('He said HaHaHa')
print(mo)

mo = strRegex.search('He said HaHaHaHaHa')
print(mo)
mo = strRegex.search('He said Ha')
print(mo)

# Unbounded range can have any times
strRegex = re.compile(r'(Ha){3,}')
mo = strRegex.search('He said HaHaHa')
print(mo)



# * zero or more

batRegex = re.compile(r'bat(wo)*man') # wo can occure 0/more any number time
mo = batRegex.search('The adventures of batman')
print(mo.group())

mo = batRegex.search('The adventures of batwoman')
print(mo.group())

mo = batRegex.search('The adventures of batwowowowoman')
print(mo.group())

# + one or more

batRegex = re.compile(r'bat(wo)+man') # wo can occure 0/more any number time
mo = batRegex.search('The adventures of batman')
print(mo)

mo = batRegex.search('The adventures of batwoman')
print(mo.group())

mo = batRegex.search('The adventures of batwowowowoman')
print(mo.group())

# \ to find literal characters
litralRegex = re.compile(r'\+\*\?')
mo = litralRegex.search('I learnt about literal +*? regex in todays session')
print(mo.group())


mo = litralRegex.search('I learnt about literal +*?+*?+*?+*? regex in todays session')
print(mo.group())