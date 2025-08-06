import json
import os

BLOB_DIR = 'blob_archive'
COSMOS_FILE = 'sample_data.json'

def read_cosmos(rec_id):
    try:
        for r in json.load(open(COSMOS_FILE)):
            if r['id'] == rec_id:
                return r
    except Exception:
        return None

def read_blob(rec_id):
    path = os.path.join(BLOB_DIR, f"{rec_id}.json")
    if os.path.exists(path):
        return json.load(open(path))
    return None

def get_record(rec_id):
    rec = read_cosmos(rec_id)
    if rec:
        print("✅ Found in Cosmos DB:", rec)
        return
    rec = read_blob(rec_id)
    if rec:
        print("📦 Found in Blob archive:", rec)
        return
    print("❌ Record not found.")

if __name__ == '__main__':
    for test_id in ['1', '2', '3']:
        get_record(test_id)
