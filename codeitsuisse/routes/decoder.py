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
    random.shuffle(pvalue)
    out = { "answer": pvalue[0:slots]}
    return json.dumps(out)