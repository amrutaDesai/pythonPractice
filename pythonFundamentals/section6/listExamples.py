spamList = ['Cat','Dog','rat','elephant']
print(spamList)
print(spamList[0])
# print(spamList[4]) # IndexError list index out of range

# List can have list inside
spamList = [['Cat','Dog','rat','elephant'],[10,20,30,40]]
print(spamList[1])
print(spamList[1][2])

# negative indexes are also possible -1 refers to last value in the list
print(spamList[-1])
print(spamList[-2])
# print(spamList[-2] + ' this is list of animals')  TypeError 'can only concatenate list (not "str") to list'
print(spamList[-2][3] + ' is afraid of ' + spamList[-2][1])

# slice of list
spamList = ['Cat','Dog','rat','elephant']
print("Slice of the list is")
print(spamList[1:3])

print('Assigning value to list')
spamList = ['Cat','Dog','rat','elephant']
spamList[1] = 10
print(spamList)

print('Assigning a slice to a list')
spamList = ['Cat','Dog','rat','elephant']
spamList[1:3] = [10,20,30,40]
print(spamList)

print('Slice shortcuts')
spamList = ['Cat','Dog','rat','elephant']
print(spamList[:2])
print(spamList[1:])

print('Delete value from list = unassignment statement')
spamList = ['Cat','Dog','rat','elephant']
del spamList[2]
print(spamList)

print('Similarities between strings and len')
print(len(spamList))
str = 'Hello'
print(len(str))

print('Concatenation with + operator')
print([1,2,3] + [4,5,6])

print('Multiplication with * values')
print('hello' * 3)
print([1,2,3] * 3)

print('List function')
print(list('hello'))

print('in or not in operators')
print('10' in [10,20,30]) # false
print(10 in [10,20,30]) # true

print('10' not in [10,20,30]) # false
print(10 not in [10,20,30]) # false
