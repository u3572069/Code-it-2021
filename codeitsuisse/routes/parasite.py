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
        keys_list = []
        values_list = []
        indi = []
        z = []
        for z in i["interestedIndividuals"]:
            indi.append([int(i) for i in z.split(",")])
        x= case12(i["grid"], indi)
        logging.info("My x :{}".format(indi))
        keys_list = i["interestedIndividuals"]
        values_list = x[0]
        zip_iterator = zip(keys_list, values_list)
        x1 = dict(zip_iterator)
        g = i["grid"]
        out = {'room': i["room"], 'p1': x1, 'p2' : x[1], 'p3': case3(g), 'p4' : case4(g)}
        a.append(out)
    logging.info("My result :{}".format(a))
    return json.dumps(a)


def case12(grid,persons):
    time_cur = 0
    time_per_person = []
    time_overall = 0
    remaining = False
    for i in range(len(persons)):
        time_per_person.append(-1)
    changes = True

    while changes == True:

        changes = False
        time_cur+=1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3: # if infected case found
                    
                    if r!=0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = 3
                            changes = True
                    if r!=(len(grid)-1):
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = 3
                            changes = True
                    if c!=0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = 3
                            changes = True
                    if c!=(len(grid[r])-1):
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = 3
                            changes = True

        for p in range(len(persons)):
            x = persons[p][0]
            y = persons[p][1]
            if grid[x][y] == 3:
                time_per_person[p] = time_cur


    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                remaining = True
        
    if remaining == True:
        time_overall = -1
    else:
        time_overall = time_cur-1

    return [time_per_person, time_overall]

def case3(grid):
    time_cur = 0
    energy = 0
    remaining = False
    changes = True

    while changes == True:

        changes = False
        time_cur+=1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3: # if infected case found

                    if r!=0 and c!=0:
                        if grid[r-1][c-1] == 1:
                            grid[r-1][c-1] = 3
                            changes = True

                    if r!=(len(grid)-1) and c!=0:
                        if grid[r+1][c-1] == 1:
                            grid[r+1][c-1] = 3
                            changes = True

                    if r!=0 and c!=(len(grid[r])-1):
                        if grid[r-1][c+1] == 1:
                            grid[r-1][c+1] = 3
                            changes = True

                    if r!=(len(grid)-1) and c!=(len(grid[r])-1):
                        if grid[r+1][c+1] == 1:
                            grid[r+1][c+1] = 3
                            changes = True
                    
                    if r!=0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = 3
                            changes = True
                    if r!=(len(grid)-1):
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = 3
                            changes = True
                    if c!=0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = 3
                            changes = True
                    if c!=(len(grid[r])-1):
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = 3
                            changes = True


    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                remaining = True
        
    if remaining == True:
        time_overall = -1
    else:
        time_overall = time_cur

    return time_overall

def case4(grid):
    #print(grid)
    time_cur = 0
    remaining = False
    changes = True

    while changes == True:

        changes = False
        time_cur+=1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 3: # if infected case found
                    
                    if r!=0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = 3
                            changes = True
                    if r!=(len(grid)-1):
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = 3
                            changes = True
                    if c!=0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = 3
                            changes = True
                    if c!=(len(grid[r])-1):
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = 3
                            changes = True


    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                remaining = True
        
    if remaining == True:
        threeclose = []
        ones = []
        diffs= []

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
                
        return  max(diffs)-1

    else:
        return 0





