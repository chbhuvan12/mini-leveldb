

# Mini LevelDB

A **LevelDB-inspired key-value store** implemented in Python using an  
**LSM-Tree (Log-Structured Merge Tree) architecture**.

This project demonstrates how modern storage engines handle high write throughput
using **Write-Ahead Logging (WAL)**, **MemTables**, and **immutable SSTables**.

---

## 🚀 Features

- Key-Value API: `put`, `get`, `delete`
- Write-Ahead Log (WAL) for durability
- In-memory MemTable (sorted)
- Immutable SSTables on disk
- Manual flush to disk
- Crash recovery using WAL
- Simple, readable implementation

---

