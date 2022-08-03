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
