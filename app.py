from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

with open('data.json', 'r') as f:
    dl_data = json.load(f)

@app.route('/api/driving_licenses', methods=['GET'])
def get_driving_licenses():
    return jsonify(dl_data)

@app.route('/api/driving_licenses/<string:license_number>', methods=['GET'])
def get_driving_license_by_number(license_number):
    dl = next((item for item in dl_data if item["license_number"] == license_number), None)
    if dl is not None:
        return jsonify(dl)
    else:
        return jsonify({"error": "Driving license not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)