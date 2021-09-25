import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluate1():
    data = request.get_json()
    j = json.loads(data)
    logging.info("data sent for evaluation {}".format(data))
    # result = inputValue * inputValue
    out = {}
    a=[]
    x1={}
    for i in j:
        x= case1and2(i["grid"], i["interestedIndividuals"])
        for k in i["interestedIndividuals"]:
            x1[k]== 2
        out = {'room': i["room"], 'p1': x[0], 'p2' : x[1], 'p3': [], 'p4' : []}
        a.append(out)
    logging.info("My result :{}".format(a))
    return json.dumps(a)

def case1and2(grid, people):

    time_cur = 0
    time_taken = []
    healthy = False
    for i in range(len(people)):
        time_taken.append(-1)
    changes = True

    while changes == True:
        
        changes = False
        time_cur += 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3: # if infected case found
                    
                    if r!=0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = -1
                            changes = True
                    if r!=(len(grid)-1):
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = -1
                            changes = True
                    if c!=0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = -1
                            changes = True
                    if c!=(len(grid[r])-1):
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = -1
                            changes = True
    
        for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r][c] == -1):
                    grid[r][c] = 3

                    # CASE 1
                    for p in range(len(people)):
                        if r == people[p][0] and c == people[p][1]:
                            time_taken[p] = time_cur

        

    for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r][c] == 1):
                    healthy = True

    # CASE 2
    if healthy == True:
        time_full = -1
    else:
        time_full = time_cur-1

    return (time_taken, time_full)



def case3(grid):

    time_cur = 0
    healthy = False
    changes = True
    while changes == True:
        changes = False

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3: 
                    
                    if r!=0 and c!=0:
                        if grid[r-1][c-1] == 1:
                            grid[r-1][c-1] = -1
                            changes = True

                    if r!=(len(grid)-1) and c!=0:
                        if grid[r+1][c-1] == 1:
                            grid[r+1][c-1] = -1
                            changes = True

                    if r!=0 and c!=(len(grid[r])-1):
                        if grid[r-1][c+1] == 1:
                            grid[r-1][c+1] = -1
                            changes = True

                    if r!=(len(grid)-1) and c!=(len(grid[r])-1):
                        if grid[r+1][c+1] == 1:
                            grid[r+1][c+1] = -1
                            changes = True

                    if r!=0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = -1
                            changes = True

                    if r!=(len(grid)-1):
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = -1
                            changes = True

                    if c!=0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = -1
                            changes = True

                    if c!=(len(grid[r])-1):
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = -1
                            changes = True
                    
        for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r][c] == -1):
                    grid[r][c] = 3

        time_cur += 1

    for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r][c] == 1):
                    healthy = True

    if healthy == True:
        time_full = -1
    else:
        time_full = time_cur

    return (time_full)



def case4(grid):
    energy = 0
    changes = True
    sumthin = True
    while changes == True:

        sumthin = False
        

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3: # if infected case found
                    
                    if r!=0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = -1
                    if r!=(len(grid)-1):
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = -1
                    if c!=0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = -1
                    if c!=(len(grid[r])-1):
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = -1
    
        for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r][c] == 1):
                    sumthin = True
        
        if sumthin == True:
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 3: # if infected case found
                        
                        if r!=0:
                            if grid[r-1][c] == 0 or grid[r-1][c] == 2:
                                grid[r-1][c] = -1
                                energy +=1
                        if r!=(len(grid)-1):
                            if grid[r+1][c] == 0 or grid[r+1][c] == 2:
                                grid[r+1][c] = -1
                                energy +=1
                        if c!=0:
                            if grid[r][c-1] == 0 or grid[r][c-1] == 2:
                                grid[r][c-1] = -1
                                energy +=1
                        if c!=(len(grid[r])-1):
                            if grid[r][c+1] == 0 or grid[r][c+1] == 2:
                                grid[r][c+1] = -1
                                energy +=1

        for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r][c] == -1):
                    grid[r][c] = 3
        if sumthin == False:
            changes = False

    return (energy)



grid = [
        [0, 3, 2],
      [0, 1, 1],
      [1, 0, 0]
    ]

observe = [[0,0]]

p1,p2 = case1and2(grid,observe)
print(p1,"\n",p2)
p3 = case3(grid)
print(p3)
p4 = case4(grid)
print(p4)
