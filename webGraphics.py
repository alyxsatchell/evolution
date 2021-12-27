import json
from flask import send_from_directory
from flask import Flask, jsonify
import os

app = Flask(__name__, static_url_path='/static')

def loadPos():
    with open('popData.json', 'r') as fp:
        data = json.load(fp)
        return data

def loadArch():
    with open('archive.json', 'r') as fp:
        data = json.load(fp)
        return data

def loadPlant():
    with open('plantData.json', 'r') as fp:
        data = json.load(fp)
        return data

@app.route("/evosim/evo/popArray")
def webExecute():
    data = loadPos()
    return jsonify(data = data)

@app.route("/evo/archive")
def archiveFill():
    data = loadArch()
    return jsonify(data = data)

@app.route("/evo/plantData")
def plantDataFill():
    data = loadPlant()
    return jsonify(data = data)

@app.route('/favicon.ico')
def favicon():
    file_path = os.path.join(os.getcwd(), "static")
    return send_from_directory(file_path,
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    host_value = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port_value = 5000
    print("Starting server on {host_value}:{port_value}...")
    app.run()
