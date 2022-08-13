# Regex_Nutshell
Python Regex In a Nutshell

### Author:
Milad Sadeghi DM - [EverLookneverSee@GitHub](https://elns.info)

### General Examples:
* Example 1: find 'abc' --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L36-L46)
* Example 2: find 'abc' - Ignoring case sensitivity --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L48-L56)
* Example 3: find '.' --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L59-L67)
* Example 4: find 'elns.info' url --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L70-L78)
* Example 5: '.' --> Any character except new line --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L81-L89)
* Example 6: \d --> Digit (0-9) --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L92-L100)
* Example 7: \D --> Non-Digit (0-9) --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L103-L111)
* Example 8: \w --> Word character (a-z) (A-Z) (0-9) _ --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L114-L122)
* Example 9: \W --> Non-Word character --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L125-L133)
* Example 10: \s --> Whitespace character (space, tab, newline) --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L136-L144)
* Example 11: \S --> Non-Whitespace character --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/bc9cf8bcd09c002b0795649632cc2e4b5e5d65b8/general.py#L147-L155)
* Example 12: \b --> Word boundary --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L161-L176)
* Example 13: \B --> Non-Word boundary --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L179-L187)
* Example 14: ^ --> Beginning of a string --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L190-L198)
* Example 15: $ --> End of a string --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L201-L209)
* Example 16: \d\d\d.\d\d\d.\d\d\d\d --> Finding phone numbers --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L212-L220)
* Example 17: \d\d\d[-.]\d\d\d[-.]\d\d\d\d --> Finding phone numbers using character set-1 --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L223-L231)
* Example 18: [89]00[-.]\d\d\d[-.]\d\d\d\d --> Finding phone numbers using character set-2 --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/e346aacce8593da21630351bb0fcd2e1f923b2ee/general.py#L234-L243)
* Example 19: [1-5] --> Finding all digits between 1 and 5 --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L251-L259)
* Example 20: [a-z] --> Finding all lowercase letters --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L262-L270)
* Example 21: [A-Z] --> Finding all uppercase letters --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L273-L281)
* Example 22: [a-zA-Z] --> Finding all letters --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L284-L292)
* Example 23: [^a-zA-Z] --> Finding all non-letters --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L295-L303)
* Example 24: [^b]at --> Finding cat mat pat except bat --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L306-L314)
* Example 25: \d{3}.\d{3}.\d{4} --> Finding phone numbers using quantifiers --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L317-L333)
* Example 26: Mr\.?\s[A-Z]\w* --> Finding all Mr and following names --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/5d9329631d77e1701098640d79d843cfb7ea8d0a/general.py#L336-L344)
* Example 27 - v1: M(r|s|rs)\.?\s[A-Z]\w* --> Finding all Mr,Ms, Mrs and following names using grouping feature --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/716bed781e4dd3572e99311fd952ba882d4ef6f3/general.py#L351-L359)
* Example 27 - v2: (Mr|Ms|Mrs)\.?\s[A-Z]\w* --> Finding all Mr,Ms, Mrs and following names using grouping feature --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/716bed781e4dd3572e99311fd952ba882d4ef6f3/general.py#L362-L370)
* Example 28: [a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu) --> Fining all email addresses that are located in text --> [view source code](https://github.com/EverLookNeverSee/regex_nutshell/blob/716bed781e4dd3572e99311fd952ba882d4ef6f3/general.py#L373-L381)


#### Work in Progress ...
