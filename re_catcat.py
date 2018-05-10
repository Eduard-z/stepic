import sys
import re

"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""

for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.findall(r'cat.*cat', line):
        print(line)
