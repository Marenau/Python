class HashTable:
    def __init__(self):
        self.size = 10
        self.data = [[] for _ in range(self.size)]

    def __getitem__(self, key):
        index = self._get_index(key)
        for k, v in self.data[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        index = self._get_index(key)
        for i, (k, v) in enumerate(self.data[index]):
            if k == key:
                self.data[index][i] = (key, value)
                break
        else:
            self.data[index].append((key, value))

    def __len__(self):
        return sum(len(lst) for lst in self.data)

    def _get_index(self, key):
        return hash(key) % self.size

table = HashTable()

table['one'] = 42
table['two'] = 35
table['three'] = "Hello, world!"

print(table['one'])
print(table['two'])
print(table['three'])

print(len(table))