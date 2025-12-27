import os
from memtable import MemTable
from sstable import SSTable

class MiniLevelDB:
    def __init__(self, data_dir="data", wal_file="wal.log"):
        self.memtable = MemTable()
        self.wal_file = wal_file
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.sstables = []
        self._recover()

    def _recover(self):
        if not os.path.exists(self.wal_file):
            return

        with open(self.wal_file, "r") as f:
            for line in f:
                parts = line.strip().split(" ", 2)
                if parts[0] == "PUT":
                    self.memtable.put(parts[1], parts[2])
                elif parts[0] == "DEL":
                    self.memtable.delete(parts[1])

    def put(self, key, value):
        # WAL write (FORCES wal.log creation)
        with open(self.wal_file, "a") as f:
            f.write(f"PUT {key} {value}\n")

        self.memtable.put(key, value)

    def get(self, key):
        val = self.memtable.get(key)
        if val is not None:
            return val

        for sstable in reversed(self.sstables):
            val = sstable.read(key)
            if val is not None:
                return val
        return None

    def delete(self, key):
        with open(self.wal_file, "a") as f:
            f.write(f"DEL {key}\n")
        self.memtable.delete(key)

    def flush(self):
        filename = os.path.join(self.data_dir, f"sst_{len(self.sstables)}.txt")
        sstable = SSTable(filename)
        sstable.write(self.memtable.items())
        self.sstables.append(sstable)
        self.memtable.clear()
        open(self.wal_file, "w").close()
