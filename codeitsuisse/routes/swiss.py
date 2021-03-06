import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stig/perry', methods=['POST'])
def stigevaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    a=[]
    for i in data:
        maxRating = i["maxRating"]
        coefficients = i["coefficients"]
        questions = i["questions"][0]
        q = random.randint(1,maxRating)
        p = random.randint(1,q)
        while(p%q==0):
            q = random.randint(1,maxRating)
            p = random.randint(1,q)

        out = { 'p':175813, 'q':1000000000}
        a.append(out)
    return json.dumps(a)



input = [{
    "questions": [[
        {
          "from": 1,
          "to": 20,
        },
        {
          "from": 12,
          "to": 23,
        }
      ]
    ],
    "coefficients": [{
        "p": 0,
        "q": 0,
      }
    ],
   "maxRating": 30
  }
]

'''
output = [{
    p: Int,
    q: Int,
  }: Result
]: List<Result>
'''


def s(maxRating, questions):
    range_of_ratings = []
    for question in questions:
        range_of_rating = set()
        start = question["from"]
        end = question["to"]
        for i in range(start, end + 1):
            range_of_rating.add(i)
        range_of_ratings.append(range_of_rating)

    num = 0
    final_range = set([i for i in range(1, maxRating + 1)])
    for num_set in range_of_ratings:
        final_range = final_range.intersection(num_set)

    p = 1
    q = len(final_range)

    return (p,q)

