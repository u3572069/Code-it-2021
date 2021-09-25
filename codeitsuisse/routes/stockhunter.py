import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stockhunter', methods=['POST'])
def sevaluate():
    input = request.get_json()
    logging.info("data sent for evaluation {}".format(input))
    griddepth = input[0]["gridDepth"]
    gridkey = input[0]["gridKey"]
    horizontalStepper = input[0]["horizontalStepper"]
    verticalStepper = input[0]["verticalStepper"]

    entry = input[0]["entryPoint"]
    entry_x = entry["first"]
    entry_y = entry["second"]

    target = input[0]["targetPoint"]
    target_x = target["first"]
    target_y = target["second"]

    rect_diff_x = abs(entry_x - target_x)
    rect_diff_y = abs(entry_y - target_y)
    grid_cost = create_grid_cost(rect_diff_x, rect_diff_y, griddepth, gridkey, horizontalStepper, verticalStepper)
    min = minCost(grid_cost, target_x , target_y)
    grid = create_grid(rect_diff_x, rect_diff_y, griddepth, gridkey, horizontalStepper, verticalStepper)
    out = { "gridMap": grid, "minimumCost": min}
    return json.dumps(out)

    


import sys

input = [{
    "entryPoint":{
        "first": 0,
        "second": 0
        },
    "targetPoint":{
        "first": 2,
        "second": 2
        },
    "gridDepth": 156,
    "gridKey":20183,
    "horizontalStepper":16807,
    "verticalStepper":48271
}]

'''
FORMULAE:

1. risk-index[x,0] = x*hor_st
2. risk-index[0,y] = y*ver_st
3. risk-index[x,y] = risklevel[x-1,y] * risklevel[x,y-1]
4. risk-cost = risklevel%3 - 3:L, 2:M, 1:S
5. risklevel = [risk-index + depth]%Gridkey
'''



def riskindex(point, horizontalStepper, verticalStepper, griddepth, gridkey):

    if point[1] == 0:
        return Xriskindex(point, horizontalStepper)
    if point[0] == 0:
        return YriskIndex(point, verticalStepper)
    else:
        return risklevel([point[0]-1,point[1]], griddepth, gridkey, horizontalStepper, verticalStepper)*risklevel([point[0],point[1]-1], griddepth, gridkey, horizontalStepper, verticalStepper)

def Xriskindex(point, horizontalStepper):
    return point[0] * horizontalStepper

def YriskIndex(point, verticalStepper):
    return point[1] * verticalStepper

def risklevel(point, griddepth, gridkey, horizontalStepper, verticalStepper):
    return (riskindex(point, horizontalStepper, verticalStepper, griddepth, gridkey)+griddepth)%gridkey

def riskcost(point, griddepth, gridkey, horizontalStepper, verticalStepper):
    x = risklevel(point, griddepth, gridkey, horizontalStepper, verticalStepper)%3
    if x == 0:
        return 3
    elif x == 1:
        return 2
    elif x ==2:
        return 1

def riskcategory(point, griddepth, gridkey, horizontalStepper, verticalStepper):
    x = riskcost(point, griddepth, gridkey, horizontalStepper, verticalStepper)
    if x == 3:  return 'L'
    if x == 2:  return 'M'
    if x == 1:  return 'S'

# Minimum Costs
def minCost(cost, target_x,target_y):
    if (target_y < 0 or target_x < 0):
        return sys.maxsize
    elif (target_x == 0 and target_y == 0):
        return cost[target_x][target_y]
    else:
        return cost[target_x][target_y] + min( minCost(cost, target_x-1, target_y-1),
                                minCost(cost, target_x-1, target_y),
                                minCost(cost, target_x, target_y-1) )

def min(x, y, z):
    if (x < y):
        return x if (x < z) else z
    else:
        return y if (y < z) else z


def create_grid(rect_diff_x, rect_diff_y, griddepth, gridkey, horizontalStepper, verticalStepper):

    grid = []
    grid_row = []
    for y in range(rect_diff_x + 1):
        for x in range(rect_diff_y + 1):
            grid_row.append(riskcategory([x, y], griddepth, gridkey, horizontalStepper, verticalStepper))
        grid.append(grid_row)
        grid_row = []

    return grid

def create_grid_cost(rect_diff_x, rect_diff_y, griddepth, gridkey, horizontalStepper, verticalStepper):

    grid = []
    grid_row = []
    for y in range(rect_diff_x + 1):
        for x in range(rect_diff_y + 1):
            grid_row.append(riskcost([x, y], griddepth, gridkey, horizontalStepper, verticalStepper))
        grid.append(grid_row)
        grid_row = []

    return grid




 

# Driver program to test above functions












