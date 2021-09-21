def regularExpresionBasics():
    print("""
    1. Regex String often use \ backslashes like \d so they are often raw string
    2. import the re module first
    3. Call the re.compile object to create regex object
    4. Call the regex object's search method to create a matched object
    5. Call the match object's group method to create the match String
    6. \d is the regex for a numeric digit character.
    7. You can make your own character classes with square brackets: [aeiou]
    8. A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]
    """)


def MethodOnRegexObject() :
    print('''
    1. search              returns matched object & find first matched object
    2. findall()           returns list of string / list of tuples of strings & Finds all matched object
    ''')


regularExpresionBasics()

