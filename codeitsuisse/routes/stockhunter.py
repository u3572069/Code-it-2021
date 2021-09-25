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
        x = minCost(riskcost, target_x, target_y)
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
        grid[i][0] = i * horizontalStepper
    for j in range(len(grid[0])):
        grid[0][j] = j * verticalStepper
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
   # initialization
   tc = [[0 for x in range(len(cost))] for x in range(len(cost[0]))]
   # base case
   tc[0][0] = cost[0][0]
   # total cost(tc) array
   for i in range(1, m + 1):
      tc[i][0] = tc[i-1][0] + cost[i][0]
   # tc array
   for j in range(1, n + 1):
      tc[0][j] = tc[0][j-1] + cost[0][j]
   # rest tc array
   for i in range(1, m + 1):
      for j in range(1, n + 1):
         tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
   return tc[m][n]
















