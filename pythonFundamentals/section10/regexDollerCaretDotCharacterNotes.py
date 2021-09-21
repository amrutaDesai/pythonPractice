def dollerCaretDotCharacterNotes():
    print("""
    1. ^ means the string must start with pattern, $ means the string must end with the 
    2. pattern. Both means the entire string must match the entire pattern.
    3. The . dot is a wildcard; it matches any character except newlines.
    4. Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
    5.Pass re.I as the second argument to re.compile() to make the matching case-insensitive.
    """)

dollerCaretDotCharacterNotes()