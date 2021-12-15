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

@app.route("/evo/popArray")
def webExecute():
    data = loadPos()
    return jsonify(data = data)

@app.route("/evo/archive")
def archiveFill():
    data = loadArch()
    return jsonify(data = data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, r'C:\Users\x2\Documents\GitHub\evolution\static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    #host_value = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    #port_value = 5000
    print("Starting server on {host_value}:{port_value}...")
    app.run()
