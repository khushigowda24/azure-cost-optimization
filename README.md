

## Task Overview

The assignment involved creating a Python solution to optimize Azure cost management by archiving old records from Cosmos DB to Blob storage as an archival system. The goal was to:

* Identify and archive records older than a certain date from Cosmos DB to Blob storage.
* Implement a fallback mechanism to read data from Blob storage if records are not found in Cosmos DB.
* Demonstrate the archival and fallback reading process through executable scripts.

---

## Solution Delivered

archive\_old\_records.py: Script to archive records older than a given date from Cosmos DB to Blob storage. The script successfully archives old records and removes them from the primary database.
read\_fallback\_example.py: Script demonstrating how to read records, first trying to retrieve from Cosmos DB and falling back to Blob storage archive if the record is not found.
Sample data and Blob storage JSON files were used to simulate the data and the archive.


## Sample Output

When running the archive script, it outputs the number of records archived:
Archived 2 record(s).


When running the fallback reading script, it outputs records found either in Blob storage or Cosmos DB:
📦 Found in Blob archive: {'id': '1', 'customerId': 'custA', 'created': '2025-04-01', 'amount': 100}
📦 Found in Blob archive: {'id': '2', 'customerId': 'custB', 'created': '2025-01-15', 'amount': 150}
✅ Found in Cosmos DB: {'id': '3', 'customerId': 'custA', 'created': '2025-06-01', 'amount': 200}

