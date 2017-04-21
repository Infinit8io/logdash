from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.code import Code
from flask import jsonify
from flask_cors import CORS, cross_origin
from bson.json_util import dumps
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
    reducer = Code("""
                    function(obj, prev){}
                    """)
    data = logs.group(
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

@app.route('/machine/<string:machine_slug>')
@cross_origin()
def get_machine(machine_slug):
    data = logs.find({"machine_slug": machine_slug}).sort("metrics_took_at").limit(10)
    return dumps(data, indent=4),200, {'Content-Type':'application/json'}


@app.route('/machine/<string:machine_slug>/<float:date_begin>/<float:date_end>')
@cross_origin
def get_machine_dates(machine_slug, date_begin, date_end):
    data = logs.find({"machine_slug": machine_slug, "metrics_took_at": {"$gt" : date_begin, "$lt": date_end} }).sort("metrics_took_at").limit(10)
    return dumps(data, indent=4),200, {'Content-Type':'application/json'}

@app.route('/')
def index():
    return "Lol"
