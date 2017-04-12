from flask import Flask
from flask import request
from pymongo import MongoClient

import json

client = MongoClient()
db = client.logdashDB
logs = db.logs

app = Flask(__name__)

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

@app.route('/machines', method=['GET'])
def show_machines():
    print("TAKE MY MACHINES")
'''
    name
    sysname
    mac
    slug
    nb_cpu
    memory
    ip
'''
