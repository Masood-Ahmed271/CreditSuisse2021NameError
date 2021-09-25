import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluatefixedrace():
    data = request.get_data()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result =""
#     racers = data.split(",")
#     result = fixedrace(racers)

    return result

    # logging.info("My result :{}".format(result))
    # return jsonify(result)



# def fixedrace(racers):
# #     random.shuffle(racers)
# #     return (','.join(racers))
#     return ""
    
