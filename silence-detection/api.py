from flask import jsonify, request, session

app_silence_detect = Flask(__name__)
CORS(app_silence_detect)
app_silence_detect.secret_key = 'some random string'

@app_silence_detect.route("/silence/heartbeat", methods=['GET'])
def get_route():
	return jsonify({"algorithm": "sulence-detect", "status": "Running"}), 200

@app_silence_detect.route("/silence/helloworld", methods=['GET'])
def get_route():
	return jsonify({"response":"Hello world"}, 200)
