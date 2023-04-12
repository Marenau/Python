class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__hidden = 42

obj = MyClass(1, 2)

attrs = dir(obj)

field_names = [name for name in attrs if not name.startswith('__')]

print(field_names)

print(obj.__dict__, end="\n")

print(vars(obj))