# x = input().split()
# xs = (int(i) for i in x)

# def even(x):
#     x % 2 == 0

# even = lambda x: x % 2 == 0

# evens = list(filter(even, xs))
# print(evens)

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]


def length(name):
    return len(" ".join(name))

name_length = [length(name) for name in x]
print(name_length)

x.sort(key=length)  # x.sort(key=lambda name: len(" ".join(name)))
print(x)

# import operator as op
# x.sort(key=op.itemgetter(-1))  # sort by last element
# print(x)


# import operator as op
# from functools import partial

# sort_by_last = partial(list.sort, key=op.itemgetter(-1))  # sort by last element
# print(x)
# sort_by_last(x)
# print(x)
