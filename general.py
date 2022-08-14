"""
    General Regular Expressions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    A collection of general regular expressions.
    All of these are based on the Python re module.
    Author: Milad Sadeghi DM - EverLookNeverSee@GitHub
"""

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

elns.info

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Sadeghi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

MiladSadeghiDM@gmail.com
milad.sadeghi@university.edu
milad-123-sadeghi@my-job.net

https://www.google.com
http://www.udacity.com
https://elns.info
https://www.nasa.gov
'''

urls = """
https://www.google.com
http://www.udacity.com
https://elns.info
https://www.nasa.gov
"""

sentence = 'Start a sentence and then bring it to an end'

# Example 1:
print("Example 1:")
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")


print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 2:
print("Example 2:")
pattern = re.compile(r'abc', re.IGNORECASE)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 3:
print("Example 3:")
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 4:
print("Example 4:")
pattern = re.compile(r'elns\.info')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 5: . --> Any character except newline
print("Example 5: . --> Any character except newline")
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 6: \d --> Digit (0-9)
print("Example 6: \d --> Digit (0-9)")
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 7: \D --> Not a digit (0-9)
print("Example 7: \D --> Not a digit (0-9)")
pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 8: \w --> Word character (a-z) (A-Z) (0-9) _
print("Example 8: \w --> Word character (a-z) (A-Z) (0-9) _")
pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 9: \W --> Not a word character
print("Example 9: \W --> Not a word character")
pattern = re.compile(r'\W')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 10: \s --> Whitespace (space, tab, newline)
print("Example 10: \s --> Whitespace (space, tab, newline)")
pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 11: \S --> Not whitespace (space, tab, newline)
print("Example 11: \S --> Not whitespace (space, tab, newline)")
pattern = re.compile(r'\S')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 12: \b --> Word boundary.
"""
    There are three different positions that qualify as word boundaries:
    1. Before the first character in the string, if the first character is a word character.
    2. After the last character in the string, if the last character is a word character.
    3. Between two characters in the string, where one is a word character and the other
        is not a word character.
"""
print("Example 12: \b --> Word boundary.")
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 13: \B --> Not a word boundary.
print("Example 13: \B --> Not a word boundary.")
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 14: ^ --> The beginning of a string.
print("Example 14: ^ --> The beginning of a string.")
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {sentence[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 15: $ --> The end of a string.
print("Example 15: $ --> The end of a string.")
pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {sentence[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 16: Finding phone numbers.
print("Example 16: Finding phone numbers.")
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 17: Finding phone numbers using character set.
print("Example 17: Finding phone numbers using character set.")
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 18: Finding phone numbers using character set.
# Finding these two numbers: 800-555-1234 and 900-555-1234
print("Example 18: Finding phone numbers using character set.")
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 19: Finding all digits between 1 and 5.
print("Example 19: Finding all digits between 1 and 5.")
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 20: Finding all lowercase alphabet characters.
print("Example 20: Finding all lowercase alphabet characters.")
pattern = re.compile(r'[a-z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 21: Finding all uppercase alphabet characters.
print("Example 21: Finding all uppercase alphabet characters.")
pattern = re.compile(r'[A-Z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 22: Finding all lowercase and uppercase alphabet characters.
print("Example 22: Finding all lowercase and uppercase alphabet characters.")
pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 23: Negate all lowercase and uppercase alphabet characters.
print("Example 23: Negate all lowercase and uppercase alphabet characters.")
pattern = re.compile(r'[^a-zA-Z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 24: Finding cat mat pat except bat.
print("Example 24: Finding cat mat pat except bat.")
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Quantifiers:
# * --> Zero or more times.
# + --> One or more times.
# ? --> Zero or one times.
# {n} --> Exactly n times.
# {n,} --> n or more times.
# {n,m} --> n to m times.

# Example 25: Finding phone numbers using quantifiers.
print("Example 25: Finding phone numbers using quantifiers.")
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 26: Finding all Mr and following names.
print("Example 26: Finding all Mr and following names.")
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 27 - v1: Finding all Mr,Ms, Mrs and following names using grouping feature.
print("Example 27 - v1: Finding all Mr,Ms, Mrs and following names using grouping feature.")
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 27 - v2: Finding all Mr,Ms, Mrs and following names using grouping feature.
print("Example 27 - v2: Finding all Mr,Ms, Mrs and following names using grouping feature.")
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 28: Fining all email addresses that are located in text.
print("Example 28: Fining all email addresses that are located in text.")
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu)')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 29: Fining all urls that are located in text.
print("Example 29: Fining all urls that are located in text.")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"Found characters in text: {text_to_search[match.start():match.end()]}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 30: Fining all urls that are located in text and capture information using groups.
print("Example 30: Fining all urls that are located in text and capture information using groups.")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match span indexes: {match.span()},   "
          f"group_0: {match.group(0)}     group_1: {match.group(1)}     group_2: {match.group(2)}"
          f"     group_3: {match.group(3)}")

print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 31: Reformatting the text using substitution.
print("Example 31: Reformatting the text using substitution.")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 32: Using findall to find all urls in text.
print("Example 32: Using findall to find all urls in text.")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.findall(text_to_search)
for match in matches:
    print(f"Match span indexes: {match}")
print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 33: Using group in findall method.
print("Example 33: Using group in findall method.")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.findall(text_to_search)
for match in matches:
    print(f"Group_0: {match[0]}     group_1: {match[1]}     group_2: {match[2]}")
print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 34: Using match method in order to match the beginning of the string.
print("Example 34: Using match method in order to match the beginning of the string.")
pattern = re.compile(r'Start')
matches = pattern.match(sentence)
print(matches)
print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 35: Using search method in order to search entire of the string.
print("Example 35: Using search method in order to search entire of the string.")
pattern = re.compile(r'sentence')
matches = pattern.search(sentence)
print(matches)
print("*" * 65)
# ----------------------------------------------------------------------------------

# Example 36: Using ignore case flag.
print("Example 36: Using ignore case flag.")
pattern = re.compile(r'start', re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)
print("*" * 65)
# ----------------------------------------------------------------------------------
