# Dictionary = {key:value}
# an unordered collection of data values

spam={'size':'fat','color':'gray','disposition':'loud'}
print(spam['size'])

# Dictionary has no order
spam={'size':'big','count':'10','color':'white'}
eggs={'count':'10','size':'big','color':'white'}
print(spam == eggs)

# KeyError on accessing non existing key
#print(spam['name'])

"""
Traceback (most recent call last):
  File "/Users/AMGA/Desktop/python_practice/pythonFundamentals/section7/directoryPractice.py", line 12, in <module>
    print(spam['name'])
KeyError: 'name'
"""

# in or not in operator for dictionaries
print('**** in not in operator in dictionary python ***')
print('name' in spam)
print('size' in spam)
print('size' not in spam)

# Dictionaries are mutable functions keys(), values(), items()

print(spam.keys())
# dict_keys(['size', 'count', 'color'])

print(list(spam.keys()))
# ['size', 'count', 'color']

print(spam.values())
print(spam.items()) # returns the list of all dictionary keys with values

for k in spam.keys() :
    print(k)
for k,v in spam.items() :
    print(k + ' value is ' + v)

    for k in spam.items() :
        print(k) # returns tuple, immutable , with curly brackets

#get some value if the key does not exist in the dictionary to avoid error

print(spam.get('size'))
print(spam.get('name'),0)

# Setting values
if 'name' not in spam :
    spam['name'] = 'ABC'

print(spam)

