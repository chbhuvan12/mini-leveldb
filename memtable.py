from sortedcontainers import SortedDict

class MemTable:
    def __init__(self):
        self.table = SortedDict()

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)

    def delete(self, key):
        self.table[key] = None  # tombstone

    def items(self):
        return self.table.items()

    def clear(self):
        self.table.clear()
