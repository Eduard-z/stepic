import re
"""
pattern = r'abc'
string = "babcd"
match_object = re.match(pattern, string)  # совпадение с начала
print(match_object)
search_object = re.search(pattern, string)  # совпадение в любом месте
print(search_object)
"""

"""
pattern = r'a[abc]c'
string = "acc, abc, aac"
all_inclusions = re.findall(pattern, string)  # ['acc', 'abc', 'aac']
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string)  # abc, abc, abc
print(fixed_typos)
"""

# [] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]

"""
pattern = r'a.c'
string = "abcd"
match_object = re.match(pattern, string)  # совпадение с начала
print(match_object)

string = "acc, a.c, aac, aXc"
all_inclusions = re.findall(pattern, string)  # ['acc', 'a.c', 'aac', 'aXc']
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string)  # abc, abc, abc, abc
print(fixed_typos)
"""

"""
# pattern = r'ab*a'  # ['aa', 'aba', 'abba', 'abbba', 'abbbba']
# pattern = r'ab+a'  # ['aba', 'abba', 'abbba', 'abbbba']
# pattern = r'ab?a'  # ['aa', 'aba']
# pattern = r'ab{3}a'  # ['abbba']
# pattern = r'ab{2,4}a'  # ['abba', 'abbba', 'abbbba']
# pattern = r'ab{,3}a'  # ['aa', 'aba', 'abba', 'abbba']
string = "aa, aba, abba, abbba, abbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
"""

"""
pattern = r"a[ab]+a"  # ['abaaba']
pattern = r"a[ab]+?a"  # ['aba', 'aba']
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))
"""

"""
pattern = r"((abc)|(test|text)*)"
string = "testtext"
print(re.match(pattern, string))
print(re.match(pattern, string).groups())  # ('testtext', None, 'text')
"""

"""
pattern = r"Hello (abc|text)"
string = "Hello abc"
print(re.match(pattern, string))
print(re.match(pattern, string).group(0))  # Hello abc
print(re.match(pattern, string).group(1))  # abc
"""

"""
pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)  # [('test-test', 'test'), ('chow-chow', 'chow')]
print(duplicates)
"""


x = re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG)
print(x)
