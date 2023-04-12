class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

obj = MyClass(3, 2)

method_name = "add"

method = getattr(obj, method_name)

result = method()

print(result)