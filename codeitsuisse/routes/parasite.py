import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluate2():
    j = request.get_json()
    logging.info("data sent for evaluation {}".format(j))
    # result = inputValue * inputValue
    out = {}
    a=[]
    
    for i in j:
        x1={}
        out={}
        x= case1and2(i["grid"], i["interestedIndividuals"])
        for k in range(0, len(i["interestedIndividuals"])):
            x1[i["interestedIndividuals"][k]]=x[0][k]
        out = {'room': i["room"], 'p1': x1, 'p2' : x[1], 'p3': case3(i["grid"]), 'p4' : x[2]}
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


    threeclose = []
    ones = []
    diffs= []
    case4_ans = 0
    #CASE 4 IN OPERATION
    if healthy == True:

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3:
                    threeclose.append([r,c])
                if grid[r][c] == 1:
                    ones.append([r,c])
                    diffs.append(999)

        for i in range(len(ones)):
            for j in range(len(threeclose)):
                if abs(threeclose[j][0]-ones[i][0]) + abs(threeclose[j][1] - ones[i][1])  < diffs[i]:
                    diffs[i] = abs(threeclose[j][0]-ones[i][0]) + abs(threeclose[j][1] - ones[i][1])
                
        case4_ans =  max(diffs) -1


    




    return (time_taken, time_full, case4_ans)












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


grid = [
        [0, 3],
        [0, 1]
    ]

observe = [[0,0]]

p1,p2,p4 = case1and2(grid,observe)
print(p1,"\n",p2)
p3 = case3(grid)
print(p3,"\n",p4)
