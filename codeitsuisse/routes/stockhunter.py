import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stock-hunter', methods=['POST'])
def sevaluate():
    sys.setrecursionlimit(10**6)
    input = request.get_json()
    a=[]
    logging.info("data sent for evaluation {}".format(input))
    for i in input:
        griddepth = i["gridDepth"]
        gridkey = i["gridKey"]
        horizontalStepper = i["horizontalStepper"]
        verticalStepper = i["verticalStepper"]

        entry = i["entryPoint"]
        entry_x = entry["first"]
        entry_y = entry["second"]

        target = i["targetPoint"]
        target_x = target["first"]
        target_y = target["second"]

        rect_diff_x = abs(entry_x - target_x)
        rect_diff_y = abs(entry_y - target_y)
        grid_cost = create_grid_cost(rect_diff_x, rect_diff_y, griddepth, gridkey, horizontalStepper, verticalStepper)
        min = minCost(grid_cost, target_x , target_y)
        grid = create_grid(rect_diff_x, rect_diff_y, griddepth, gridkey, horizontalStepper, verticalStepper)
        out = { "gridMap": grid, "minimumCost": min}
        a.append(out)
    return json.dumps(a)

    


import sys





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












