
from flask import Flask, request
import json
import requests
import ast
from model_train import train

app = Flask(__name__)

@app.route('/')
def hello():
	return "Device 2"

@app.route('/sendstatus', methods=['GET'])
def send_status():
	api_url = 'http://localhost:8000/clientstatus'

	data = {'client_id': '8002'}
	print(data)

	r = requests.post(url=api_url, json=data)
	print(r, r.status_code, r.reason, r.text)
	if r.status_code == 200:
		print("yeah")
	
	return "Status OK sent !"

@app.route('/sendmodel')
def send_model():
	file = open("/home/sarth/flask/Fedlearn-master/device2/local_model/model2.h5", 'rb')
	data = {'fname':'model2.h5', 'id':'http://localhost:8002/'}
	files = {
		'json': ('json_data', json.dumps(data), 'application/json'),
		'model': ('model2.h5', file, 'application/octet-stream')
	}
	
	req = requests.post(url='http://localhost:8004/cmodel', 
						files=files)
	req1 = requests.post(url='http://localhost:8004/cfile', 
						files=files)
	# print(req.text)
	return "Model sent !"

@app.route('/aggmodel', methods=['POST'])
def get_agg_model():
	if request.method == 'POST':
		file = request.files['model'].read()
		fname = request.files['json'].read()

		fname = ast.literal_eval(fname.decode("utf-8"))
		fname = fname['fname']
		print(fname)

		wfile = open("/home/sarth/flask/Fedlearn-master/device2/model_update/"+fname, 'wb')
		wfile.write(file)
			
		return "Model received!"
	else:
		return "No file received!"

@app.route('/modeltrain')
def model_train():
	train()
	return "Model trained successfully!"


if __name__ == '__main__':
	app.run(host='localhost', port=8002, debug=False, use_reloader=True)














