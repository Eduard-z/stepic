from functools import partial

from builtins import print

x = int("1101", base=2)
print(x)
int_2 = partial(int, base=2)
x = int_2("1101")
print(x)
