import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def devaluate4():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    pvalue = data.get("possible_values")
    slots = data.get("num_slots")
    try:
        hist = data.get("history")
        k = hist[0]
        if(k["result"]==4 or k["result"]==22 or k["result"]==13 or k["result"]==31):
            pvalue = k["output_received"]
    except:
        pass
    random.shuffle(pvalue)
    out = { "answer": pvalue[0:slots]}
    return json.dumps(out)