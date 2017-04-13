from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.code import Code
from flask import jsonify
from flask_cors import CORS, cross_origin
import json

client = MongoClient()
db = client.logdashDB
logs = db.logs

app = Flask(__name__)
CORS(app)

@app.route('/server', methods=['POST'])
def consume():
    print("CONSUMER REQUESTED")

    # This is the JSON object to save in DB
    log = request.get_json()

    # Informative print of posted data
    # print(json.dumps(log, indent=4))

    log_id = logs.insert_one(log).inserted_id

    print(log_id)
    # Return success
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run()

@app.route('/machines', methods=['GET'])
@cross_origin()
def show_machines():
    print("TAKE MY MACHINES")

    reducer = Code("""
                    function(obj, prev){}
                    """)
    data = db.logs.group(
        key={
            "machine_slug": True,
            "machine_mac": True,
            "machine_name": True,
            "machine_sysname": True,
            "metrics.memory.memory_total": True,
            "metrics.cpu.cpu_number_logical": True,
            "metrics.network": True
            },
        initial={},
        reduce= reducer,
        condition={}
    )
    return json.dumps(data), 200, {'Content-Type':'application/json'}

@app.route('/')
def index():
    return "Lol"
