def regexSubVerboseMethodNotes():
    print("""
        1.The sub() regex method will substitute matches with some other text.
        2.Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
        3.Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to 	re.compile().
        4.If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.
    """)

regexSubVerboseMethodNotes()