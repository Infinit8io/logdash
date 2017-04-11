from flask import Flask
from flask import request

import json

app = Flask(__name__)

@app.route('/consume', methods=['POST'])
def consume():
    print("CONSUMER REQUESTED")

    # This is the JSON object to save in DB
    log = request.get_json()

    # Informative print of posted data
    #print(json.dumps(log, indent=4))

    # Return success
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run()
