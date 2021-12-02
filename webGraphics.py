import json
from flask import send_from_directory
from flask import Flask, jsonify
import os

app = Flask(__name__, static_url_path='/static')

def loadPos():
    with open('popData.json', 'r') as fp:
        data = json.load(fp)
        return data

@app.route("/evo/popArray")
def webExecute():
    data = loadPos()
    return jsonify(data = data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, r'C:\Users\Nicholas\Documents\Code\evolution\static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    print("Starting server...")
    app.run()