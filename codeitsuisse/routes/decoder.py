import logging
import random
from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(_name_)

@approute('/decoder', methods=['POST'])

def evaluateDecoder():
    info = request.get_data()
    logging.info("data sent for evaluation {}".format(info))
    possible = info['possible_values']
    num = info['num_slots']
    guess = random.sample(possible, num)
    return guess
