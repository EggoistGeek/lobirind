import time
import json
import os.path

def save(row_data,user, name = 'log'):
	data = {user: row_data}
	if os.path.isfile(name+'.json'):
		with open(name+'.json', mode='r') as file:
			a: dict = file.read()
		a = json.loads(a)
		a.update(data)
		with open(name+'.json', mode='w') as file:
			file.write(json.dumps(a))
	else:
		with open(name+'.json', mode='w') as file:
			file.write(json.dumps(data))

def load(name='log'):
	if os.path.isfile(name+'.json'):
		with open(name+'.json', mode='r') as file:
			a: dict = file.read()
		return json.loads(a)

# if __main__=='__name__':
# 	save({'GPS_1':True, 'tmp_2':None})
# 	print(load())
