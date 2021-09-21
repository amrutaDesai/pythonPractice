import re

# TODO Create a regex expression for phone number
# ex 455-555-1234, (455) 555-1234 ,555-1234,555-1234 ext 12345, ext. 12345, x12345

"""
phoneRegrexExp = re.compile(r'''
(\d\d\d|(\d\d\d))? # area code (optional)
(\s|-)              # First seperator
\d\d\d              # first 3 digits
-                   # Seperator
\d\d\d\d            # last 4 digits
((ext(\.)?\s)|x)                    # ext word part(optional)
  (                  # ext number part 2-5 numbers(optional)

''',re.VERBOSE)
"""