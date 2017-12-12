d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# using zip
print(dict(zip(d.values(), d.keys())))

# OR

# using dict comprehension
print({v:k for k, v in d.items()})
