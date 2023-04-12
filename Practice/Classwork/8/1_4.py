def get_inheritance(cls):
    return ' -> '.join([c.__name__ for c in cls.__mro__])

print(get_inheritance(OSError))