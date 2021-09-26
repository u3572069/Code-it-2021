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
        riskcost = return_index(rect_diff_y, rect_diff_x, verticalStepper, horizontalStepper, griddepth, gridkey, target_x, target_y)
        riskcost2 = return_index(rect_diff_y, rect_diff_x, verticalStepper, horizontalStepper, griddepth, gridkey, target_x, target_y)
        x = minCost(riskcost2, target_x, target_y)
        maps = draw(riskcost)
        out = { "gridMap": maps, "minimumCost": x}
        a.append(out)
    logging.info("My result :{}".format(a))
    return json.dumps(a)

    







 

# Driver program to test above functions

import sys


def return_index(rect_diff_y, rect_diff_x, verticalStepper, horizontalStepper, griddepth, gridkey, target_x, target_y):
    grid = [[0 for x in range(rect_diff_y+1)] for x in range(rect_diff_x+1)]
    for i in range(len(grid)):
        grid[i][0] = i * verticalStepper
    for j in range(len(grid[0])):
        grid[0][j] = j * horizontalStepper
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
                grid[i][j] = (grid[i-1][j]+griddepth)%gridkey * (grid[i][j-1]+griddepth)%gridkey
    grid[target_x][target_y] = 0
            
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x = ((grid[i][j]+griddepth)%gridkey)%3
            if x == 0:
                grid[i][j] = 3
            elif x == 1:
                grid[i][j] = 2
            elif x ==2:
                grid[i][j] = 1
    #print(grid)
    return grid

def draw(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 3:
                grid[i][j] = "L"
            if grid[i][j] == 2:
                grid[i][j] = "M"
            if grid[i][j] == 1:
                grid[i][j] = "S"
    #print(grid)
    return grid


def minCost(cost, m, n):
    rows = len(cost)
    cols = len(cost[0])
    for i in range(1, cols):
        cost[0][i] += cost[0][i-1]
    for i in range(1, rows):
        cost[i][0] += cost[i-1][0]
    for row in range(1, rows):
        for col in range(1, cols):
            cost[row][col] += min(cost[row-1][col], cost[row][col-1])
    return cost[rows-1][cols-1] - cost[0][0]
















