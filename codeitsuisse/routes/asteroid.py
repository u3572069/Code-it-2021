import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluate1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("test_cases")
    # result = inputValue * inputValue
    out = {}
    a=[]
    x1={}
    for i in inputValue:
        x= answer(i)
        out = {'input': i, 'score': x[0], 'origin': x[1]}
        a.append(out)
    logging.info("My result :{}".format(a))
    return json.dumps(a)
    



def count(s):
    s=s+"1"
    c=1
    a=[]
    for i in range(0,len(s)-1):
        if(s[i]!=s[i+1]):
            a.append([s[i],c])
            c=1
        else:
            c+=1
    return a


def points(x1, x):
    score=1
    s2 = 0
    for i in range(0,min(len(x1), len(x))):
        s2=0
        if(x1[i][0]==x[i][0]):
            s2=x1[i][1]+x[i][1]
            if(s2>=10):
                s2*=2
            elif(s2>=7 and s2<10):
                s2*=1.5
            else:
                s2=s2
        score+=s2
    return score


def answer(s1):
    origin = -1
    max_score = 0
    for sub in range(1, len(s1)-1):
        point = points(count(s1[0:sub])[::-1], count(s1[sub+1:]))
        if(point>max_score):
            max_score = point
            origin = sub

    return([max_score, origin])
