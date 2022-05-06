from pymongo import MongoClient
from PIL import Image
import io
import os
client = MongoClient()
db = client.data

directory = 'data/'

for folder in os.listdir(directory):
	collection = db[folder]
	f_path = os.path.join(directory,folder)

	timestamp = os.path.join(f_path, 'timestamps.txt')
	timestamps = []

	with open(timestamp) as f:
	    timestamps = [line.rstrip('\n') for line in f]

	i = 0

	f_path = os.path.join(f_path, 'data')

	if(folder == 'velodyne_points'):
		continue

	if(folder == 'oxts'):
		for filename in os.listdir(f_path):
			f = os.path.join(f_path, filename)
			if os.path.isfile(f):
				with open(f) as file:
					line = file.readline()
				line.rstrip('\n')
				l = line.split(' ')
				values = {
					'lat': l[0],
					'lon': l[1],
					'alt': l[2],
					'roll': l[3],
					'pitch': l[4],
					'yaw': l[5],
					'vn': l[6],
					've': l[7],
					'vf': l[8],
					'vl': l[9],
					'vu': l[10],
					'ax': l[11],
					'ay': l[12],
					'ay': l[13],
					'af': l[14],
					'al': l[15],
					'au': l[16],
					'wx': l[17],
					'wy': l[18],
					'wz': l[19],
					'wf': l[20],
					'wl': l[21],
					'wu': l[22],
					'pos_accuracy': l[23],
					'vel_accuracy': l[24],
					'navstat': l[25],
					'numsats': l[26],
					'posmode': l[27],
					'velmode': l[28],
					'orimode': l[29],
					'timestamp': timestamps[i]
				}
				i += 1
				vid = collection.insert_one(values).inserted_id 
	else:
		for filename in os.listdir(f_path):
			f = os.path.join(f_path, filename)
			if os.path.isfile(f):
				im = Image.open(f)
				image_bytes = io.BytesIO()
				im.save(image_bytes, format='png')
				image = {
				'image': image_bytes.getvalue(),
				'timestamp': timestamps[i]
				}
				i += 1
				image_id = collection.insert_one(image).inserted_id