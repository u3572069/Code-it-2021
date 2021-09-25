import logging
import json
import random
from re import S

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def fevaluate():
    data = str(request.get_data('data'))

    data = data[3:len(data)-2]
    x = list(data.split(','))
    random.shuffle(x)
    s =""
    for i in x:
        s+=i+","
    return s[0:len(s)-1]