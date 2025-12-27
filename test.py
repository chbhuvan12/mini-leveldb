from db import MiniLevelDB
import os

print("Starting test...")

db = MiniLevelDB()

db.put("k1", "v1")
db.put("k2", "v2")
db.put("k3", "v3")

# FORCE FLUSH MANUALLY
db.flush()

print("k1 =", db.get("k1"))

print("\nFiles in folder:")
print(os.listdir("."))

if os.path.exists("data"):
    print("Files in data/:", os.listdir("data"))

print("Done.")
