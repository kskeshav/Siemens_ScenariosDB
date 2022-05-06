from pymongo import MongoClient
from PIL import Image
import io
import json
import os

client = MongoClient()
db = client.data

directory = 'data/'

collection = db["labels"]

f_path = ''
timestamp = os.path.join(f_path, 'mongo_entries.txt')
timestamps = []

with open(timestamp) as f:
    timestamps = [line.rstrip('\n') for line in f]

for entry in timestamps:
	if(entry.strip()):
		et = json.loads(entry)
		# print(type(et))
		collection.insert_one(et)