def dictionaryNotes() :
    print('1. Dictionary contains key-values pair and keys are like lists indexes')
    print('2. Dictionary are mutable, variables hold the reference to dictionary values,not the dictionary value itself')
    print('3. Dictionary are un order, there is no first key-value pair in the dictionary')
    print('4. The Keys(), values(), items() will return list like vallues of dictionarys keys, values, and both  key values respectively')
    print('5. The get method can return default of the key if a key does not exist')
    print('6. Setdefault  method can set the values if a key does not exist')
    print('7. The pprint modules pprint "Pretty print" function can display a dictionary value cleanly.')
    print('8. The pFormat() function returns a string value of this output')

def similaritiesNDifferencesListDictionary():
    print('Dictionaries and lists share the following characteristics:')
    print('''Both are mutable.
Both are dynamic. They can grow and shrink as needed.
Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.''')
    print('Dictionaries differ from lists primarily in how elements are accessed:')
    print('''List elements are accessed by their position in the list, via indexing.
Dictionary elements are accessed via keys.''')

dictionaryNotes()
similaritiesNDifferencesListDictionary()
