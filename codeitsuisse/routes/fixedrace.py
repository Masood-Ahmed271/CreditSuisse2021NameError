import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluatefixedrace():
    info = request.get_data(as_text=True)
    logging.info("data sent for evaluation {}".format(data))
    racers = info.split(',')
    random.shuffle(racers)
    rankings = ','.join(racers)
    return rankings
    
