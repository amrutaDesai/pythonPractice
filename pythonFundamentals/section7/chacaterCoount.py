# program to count letter in the text
import pprint

message = 'Im learning new language pythin, and it seems fun'
count = {}

for character in message.upper() :
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)

# pprint module for pretty printing
pprint.pprint(count)
ptest = pprint.pformat(count)
print(ptest)

