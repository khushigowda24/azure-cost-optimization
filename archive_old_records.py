import json
import os
from datetime import datetime, timedelta

CUTOFF_DAYS = 90
BLOB_DIR = 'blob_archive'
COSMOS_FILE = 'sample_data.json'

def load_data():
    return json.load(open(COSMOS_FILE))

def save_data(records):
    json.dump(records, open(COSMOS_FILE, 'w'), indent=2)

def archive():
    all_data = load_data()
    cutoff_date = datetime.now() - timedelta(days=CUTOFF_DAYS)
    stay = []
    archived = []
    for rec in all_data:
        created = datetime.fromisoformat(rec['created'])
        if created < cutoff_date:
            archived.append(rec)
        else:
            stay.append(rec)
    os.makedirs(BLOB_DIR, exist_ok=True)
    for rec in archived:
        fname = f"{rec['id']}.json"
        path = os.path.join(BLOB_DIR, fname)
        json.dump(rec, open(path, 'w'), indent=2)
    save_data(stay)
    print(f"Archived {len(archived)} record(s).")

if __name__ == '__main__':
    archive()
