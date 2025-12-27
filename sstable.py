import os

class SSTable:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, "w") as f:
            for key, value in data:
                if value is None:
                    f.write(f"{key}::DEL\n")
                else:
                    f.write(f"{key}::{value}\n")

    def read(self, key):
        if not os.path.exists(self.filename):
            return None

        with open(self.filename, "r") as f:
            for line in f:
                k, v = line.strip().split("::", 1)
                if k == key:
                    return None if v == "DEL" else v
        return None
