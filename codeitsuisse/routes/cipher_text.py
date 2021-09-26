import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/cipher-cracking', methods=['POST'])
def cevaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    a,x = find_ak(data[0])
    t = calculate(data, a)
    out = [x[1]]
    for i in t:
        out.append(i)
    logging.info("My result :{}".format(out))
    return json.dumps(out)

import hashlib

# m = hashlib.sha256()
def f(x, a):
    return '{0:.3f}'.format(round(x / (x - a), 3))

input = [{"D": 1, "X": 12321, "Y": "47c90ed5874ae5192dba5be539c5c4e60cdfb9c3f5b5db1828b19433b56c79b5", "est_mins" : 1.5}]
output = []

challenge_one = input[0]
def find_ak(challenge_one):
    challenge_one_x = int(challenge_one["X"] )
    challenge_one_y = challenge_one["Y"]





    a = 0
    k = 1
    found = False

    while(hashlib.sha256((str(k) + "::" + str(f(challenge_one_x, a))).encode()).hexdigest() != challenge_one_y):
        for i in range(challenge_one_x):
            a = i
            if(hashlib.sha256((str(k) + "::" + str(f(challenge_one_x, a))).encode()).hexdigest() == challenge_one_y):
                found = True
                break
        if(found == True):
            break
        k += 1


    return(a,k)

def calculate(chal, a):
    for challenge in chal[1:5]:
        x = int(challenge["X"])
        y = challenge["Y"]
        k = 1

        while(hashlib.sha256((str(k) + "::" + str(f(x, a))).encode()).hexdigest() != y):
            k += 1
        output.append(k)
    
    return output

# print(hashlib.sha256((str(k) + "::" + str(f(challenge_one_x, 258))).encode()).hexdigest())
# print(challenge_one_y)

# print(k)
#print(a)






