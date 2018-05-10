# print("abc" in "abcba")
#
# print("cabcd".find("abc", 1))  # индекс первого вхождения или -1
# print("cabcd"[1:].find("abc"))
#
# print("cabcd".index("abc"))  # индекс первого вхождения или ValueError
# print("cabcd".index("abe"))

# s = "The man in black fled across the desert,"
# print(s.startswith(("The woman", "The dog", "The man")))
# print(s.lower().count("the"))
# print(s.replace(",", "."))
# print(s.split(" "))
#
# s = "ababa"
# print(s.count("aba"))  # 1
# print(s.rfind("aba"))  # 2

# s = "_*__1, 2, 3, 4__*_"
# print(repr(s.rstrip("*_")))
# print(repr(s.lstrip("*_")))
# print(repr(s.strip("*_")))
#
# numbers = map(str, [1, 2, 3, 4, 5])
# print(repr(" ".join(numbers)))

# capital = "London is the capital of Great Britain"
# template = "{0} is the capital of {country}"
# print(template.format("London", country="Great Britain"))
# print(template.format("Vaduz", country="Liechtenstein"))

"""
import requests

template = "Response from {0.url} with code {0.status_code}"

res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))

res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))
"""

from random import random

x = random()
print(x)
print("{:.3}".format(x))
