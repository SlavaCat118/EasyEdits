import json

def open_file(path):
	f = open(path)
	file = json.load(f)
	f.close()

	return file

def dict_json(dictionary):
	jsons = json.dumps(dictionary, indent = 4)
	return jsons

def write_file(path, data):
	f = open(path, 'w')
	f.write(dict_json(data))
	f.close()