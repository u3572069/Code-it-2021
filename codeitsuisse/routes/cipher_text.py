import logging
import json
import math

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/cipher-cracking', methods=['POST'])
def cevaluate():
    data = request.get_json()
    output=[]
    logging.info("data sent for evaluation {}".format(data))
    for i in data[0:5]:
        output.append(calculate(int(i["X"]), int(i["D"]), i["Y"]))
    logging.info("My result :{}".format(output))
    return json.dumps(output)

import hashlib

# m = hashlib.sha256()
def f(x):
    c = 0
    for i in range(1,x):
        c+=i*0.5**i
    
    return truncate(c,3)

def truncate(t, n):
    return math.floor(t * 10 ** n) / 10 ** n


def calculate(x, d, y):
    fu = f(x)
    for k in range(1,10**d):
        if(hashlib.sha256((str(k) + "::" + str(fu)).encode()).hexdigest() != y):
            return k

# print(hashlib.sha256((str(k) + "::" + str(f(challenge_one_x, 258))).encode()).hexdigest())
# print(challenge_one_y)

# print(k)
#print(a)






