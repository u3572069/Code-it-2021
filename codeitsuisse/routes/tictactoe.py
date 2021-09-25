# import logging
# import json

# from flask import request, jsonify

# from codeitsuisse import app

# s=""

# logger = logging.getLogger(__name__)

# @app.route('/tic-tac-toe', methods=['GET'])
# def tevaluate():
#     data = request.get_json()
#     logging.info("data sent for evaluation {}".format(data))
#     inputValue = data.get("battleId")
#     s = inputValue
#     return s
# @app.route('/tic-tac-toe/play/<id>'% s, methods=['POST'])
# def tevaluate1(id):
#     data = request.get_json()
#     out = { "action": "(╯°□°)╯︵ ┻━┻"}
#     return json.dumps(out)




