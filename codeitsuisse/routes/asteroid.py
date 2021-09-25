import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluate1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    # result = inputValue * inputValue
    # logging.info("My result :{}".format(result))
    out = {}
    a=[]
    x1={}
    for i in data:
        x= maximize(i)
        out = {'input': i, 'score': x[0], 'origin': x[1]}
        a.append(out)
    return json.dumps(a)
    




import collections

    
def score_count(arr, position):
    hit_list = [arr[position]]

    score = 0

    if arr[position-1] != arr[position+1]:
        return 0
    for i in range(position+1,len(arr)):
        if arr[i] in arr[0:position]:
            hit_list.append(arr[i])
    

    hit_list = sorted(hit_list)
    arr = sorted(arr)
    dict1 = collections. Counter(arr)
    dict2 = collections. Counter(hit_list)

    dict3 = dict1.copy()
    for i in dict3:
        if i not in dict2:
            dict1.pop(i)


    values = dict1.values()
    values_list1 = list(values)
    values = dict2.values()
    values_list2 = list(values)

    #print(dict2)

    #print("BBBB: ", values_list1, values_list2)
    
    for i in range(len(values_list2)):

        if values_list2[i] != values_list1[i]:
            values_list2[i] = values_list1[i]
        #print("AAAA: ", values_list1, values_list2)
            
        if values_list2[i] >=10:
            score+= values_list2[i]*2
        elif values_list2[i] >=7:
            score+= values_list2[i]*1.5
        else:
            score+= values_list2[i]

    return score

def maximize(arr):
    max_score = 0
    pos = 0
    for i in range(1,len(arr)-1):
        cur_score = score_count(arr,i)
        if cur_score > max_score:
            max_score = cur_score
            pos = i

    return [max_score, pos]