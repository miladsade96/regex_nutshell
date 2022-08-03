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

Mr. Sadeghi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# Example 1:
print("Example 1:")
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match: {match},   In text: {text_to_search[match.start():match.end()]}")


print("*" * 85)
# ----------------------------------------------------------------------------------

# Example 2:
print("Example 2:")
pattern = re.compile(r'abc', re.IGNORECASE)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match: {match},   In text: {text_to_search[match.start():match.end()]}")

print("*" * 85)
# ----------------------------------------------------------------------------------

# Example 3:
print("Example 3:")
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match: {match},   In text: {text_to_search[match.start():match.end()]}")

print("*" * 85)
# ----------------------------------------------------------------------------------

# Example 4:
print("Example 4:")
pattern = re.compile(r'elns\.info')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(f"Match: {match},   In text: {text_to_search[match.start():match.end()]}")

print("*" * 85)
# ----------------------------------------------------------------------------------
